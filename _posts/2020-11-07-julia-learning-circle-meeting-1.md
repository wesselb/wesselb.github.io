---
layout:      post
title:       "Julia Learning Circle: JIT and Method Invalidations"
tags:        [julia, julia learning circle, computer science]
comments:    true
---

I am participating in a learning circle with the goal of gaining a better understanding of the [Julia language](https://julialang.org/).
To better retain what we learn, I will be turning my notes into small blog posts.
The posts should be simple, quick, but hopefully enjoyable reads.

The code snippets in this post are run on Julia 1.6.0-DEV.1440.

## Just-in-Time Compilation

The first time a method is run, it will [just-in-time](https://en.wikipedia.org/wiki/Just-in-time_compilation) (JIT) be compiled.
The compilation time can be measured with `@time`.

```julia
julia> A = randn(Float64, 3, 3);

julia> @time inv(A);
  0.244590 seconds (559.50 k allocations: 31.983 MiB, 2.82% gc time, 99.94% compilation time)

julia> @time inv(A);
  0.000015 seconds (4 allocations: 1.953 KiB)
```

The method `inv(::Vector{Float64})` is now compiled and fast to call.
However, for example `inv(::Vector{Float32})` is not yet compiled, and will consequently incur compilation time.

```julia
julia> A = randn(Float32, 3, 3);

julia> @time inv(A);
  0.188690 seconds (449.85 k allocations: 25.852 MiB, 96.79% compilation time)

julia> @time inv(A);
  0.000017 seconds (4 allocations: 1.125 KiB)
```

The Julia JIT is simple:
it compiles a method once the method is required.
This, however, comes at the cost of start-up time and delays during runtime.
Other approaches, like [PyPy](https://www.pypy.org/), first run the code on an interpreter, profile the code, and then compile bits of the code based on the profiling results;
this is called [profile-guided optimisation](https://en.wikipedia.org/wiki/Profile-guided_optimization) (POGO).

## Method Invalidation

Once a method is compiled, it can happen that it needs to be recompiled.
Namely, a method is compiled under certain assumptions, and these assumptions may not hold anymore as more code is loaded.

For example, suppose that a compiled method `m` uses the instance `my_add(x::Float64, y::Float64)` obtained from the implementation for `my_add(x::Real, y::Real)`.
If a direct implementation of `my_add(x::Float64, y::Float64)` is then added, the compiled method `m` needs to be recompiled to make use of this direct implementation: `m` gets _invalidated_.

Here's that example:

```julia
julia> my_add(x::Real, y::Real) = x + y
my_add (generic function with 1 method)

julia> my_sum(x::Vector{T}) where T<:Real = reduce(my_add, x; init=one(T))
my_sum (generic function with 1 method)

julia> my_sum(randn(10))
0.65443378603631
```

We then add a direct implementation for `my_add(x::Float64, y::Float64)`.
To detect the method invalidation, we use [SnoopCompile.jl](https://github.com/timholy/SnoopCompile.jl).

```julia
julia> trees = invalidation_trees(@snoopr begin
           my_add(x::Float64, y::Float64) = x + y
       end)
1-element Vector{SnoopCompile.MethodInvalidations}:
 inserting my_add(x::Float64, y::Float64) in Main at REPL[12]:2 invalidated:
   backedges: 1: superseding my_add(x::Real, y::Real) in Main at REPL[8]:1 with MethodInstance for my_add(::Float64, ::Float64) (10 children)
   1 mt_cache

julia> trees[1].backedges[end]
MethodInstance for my_add(::Float64, ::Float64) at depth 0 with 10 children

julia> show(trees[1].backedges[end]; minchildren=0, maxdepth=100)
MethodInstance for my_add(::Float64, ::Float64) (10 children)
 MethodInstance for (::Base.BottomRF{typeof(my_add)})(::Float64, ::Float64) (9 children)
  MethodInstance for _foldl_impl(::Base.BottomRF{typeof(my_add)}, ::Float64, ::Vector{Float64}) (8 children)
   MethodInstance for foldl_impl(::Base.BottomRF{typeof(my_add)}, ::Float64, ::Vector{Float64}) (7 children)
    MethodInstance for mapfoldl_impl(::typeof(identity), ::typeof(my_add), ::Float64, ::Vector{Float64}) (6 children)
     MethodInstance for _mapreduce_dim(::typeof(identity), ::typeof(my_add), ::Float64, ::Vector{Float64}, ::Colon) (5 children)
      MethodInstance for var"#mapreduce#665"(::Colon, ::Float64, ::typeof(mapreduce), ::typeof(identity), ::typeof(my_add), ::Vector{Float64}) (4 children)
       MethodInstance for (::Base.var"#mapreduce##kw")(::NamedTuple{(:init,), Tuple{Float64}}, ::typeof(mapreduce), ::typeof(identity), ::typeof(my_add), ::Vector{Float64}) (3 children)
        MethodInstance for var"#reduce#667"(::Base.Iterators.Pairs{Symbol, Float64, Tuple{Symbol}, NamedTuple{(:init,), Tuple{Float64}}}, ::typeof(reduce), ::typeof(my_add), ::Vector{Float64}) (2 children)
         MethodInstance for (::Base.var"#reduce##kw")(::NamedTuple{(:init,), Tuple{Float64}}, ::typeof(reduce), ::typeof(my_add), ::Vector{Float64}) (1 children)
          MethodInstance for my_sum(::Vector{Float64}) (0 children)
```

This shows the whole call stack.
You can interactively navigate the stack with `ascend(trees[1].backedges[end])`, which uses [Cthulhu.jl](https://github.com/JuliaDebug/Cthulhu.jl).

Let's perform some timings to see whether we can detect delays due to method invalidations.
Start up a fresh Julia REPL.

{: title="Invalidation" }
```julia
julia> using SnoopCompile

julia> x = randn(10);

julia> my_add(x::Real, y::Real) = x + y;

julia> my_sum(x::Vector{T}) where T<:Real = reduce(my_add, x; init=one(T));

julia> @time my_sum(x);
  0.023856 seconds (79.31 k allocations: 4.761 MiB, 99.88% compilation time)

julia> my_add(x::Float64, y::Float64) = x + y;

julia> @time my_sum(x);
  0.016896 seconds (53.17 k allocations: 2.952 MiB, 99.94% compilation time)
```

{: title="No Invalidation" }
```julia
julia> using SnoopCompile

julia> x = randn(10);

julia> my_add(x::Real, y::Real) = x + y;

julia> my_sum(x::Vector{T}) where T<:Real = reduce(my_add, x; init=one(T));

julia> @time my_sum(x);
  0.023979 seconds (79.31 k allocations: 4.761 MiB, 99.89% compilation time)

julia> my_add(x::Float32, y::Float32) = x + y;

julia> @time my_sum(x);
  0.000004 seconds (1 allocation: 16 bytes)
```

In the first case, where `my_add(::Float64, ::Float64)` gets invalidated, the second call of `my_sum(x)` again incurs compilation time.
This does not happen in the second case.

Lastly, we discuss one more common scenario in which method invalidations happen.
Consider

```julia
julia> f(x::Int) = 1;

julia> g(x) = f(x);

julia> g("1")
ERROR: MethodError: no method matching f(::String)
Closest candidates are:
  f(::Int64) at REPL[8]:1
Stacktrace:
 [1] g(x::String)
   @ Main ./REPL[9]:1
 [2] top-level scope
   @ REPL[10]:1
```

The compiled method instance `g(::String)` gives back a `MethodError`.
In particular, it assumes that there is no implementation for `f(::String)`.
If we add that implementation, then `g(::String)` needs to be recompiled to make use of the then-available `f(::String)`.
Invalidations of this kind link back to the method table.
They show up in the property `mt_backedges` of `MethodInvalidations`:

```julia
julia> invalidation_trees(@snoopr begin f(x::String) = 1 end)
1-element Vector{SnoopCompile.MethodInvalidations}:
 inserting f(x::String) in Main at REPL[11]:1 invalidated:
   mt_backedges: 1: signature Tuple{typeof(f), String} triggered MethodInstance for g(::String) (0 children)
```


