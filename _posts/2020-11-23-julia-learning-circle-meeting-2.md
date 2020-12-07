---
layout:      post
title:       "Julia Learning Circle: Memory Allocations and Garbage Collection"
tags:        [julia, julia learning circle, computer science]
comments:    true
---

## Immutable and Mutable Types

Concrete types in Julia are either immutable or mutable.
Immutable types are created with `struct ImmutableType` and mutable types are created with `mutable struct MutableType`.
The advantage of immutable types is that they can be allocated on the _stack_ as opposed to on the _heap_.
Allocating objects on the stack is typically more performant due to cache locality and the stack's simple, but more rigid memory structure.

An interesting situation occurs when an _immutable_ type references a _mutable_ type.
[Since Julia 1.5, such immutable types can be allocated on the stack.](https://github.com/JuliaLang/julia/blob/release-1.5/NEWS.md#compilerruntime-improvements)

```julia
julia> struct A
           data::Vector{Float64}
       end

julia> a = A(randn(3))
A([0.9462871255469765, 1.1995018446247545, 0.7153882414691778])
```

Here `A` is immutable, but references a `Vector{Float64}`, which is mutable.
This means that `a.data` cannot be changed, but, since `a.data` is mutable, e.g. `a.data[1]` _can_ be changed.

```julia
julia> a.data = randn(3)
ERROR: setfield! immutable struct of type A cannot be changed
Stacktrace:
 [1] setproperty!(x::A, f::Symbol, v::Vector{Float64})
   @ Base ./Base.jl:34
 [2] top-level scope
   @ REPL[5]:1

julia> a.data[1] = 1.0
1.0
```

Types `T` that satisfy `isbitstype(T) == true` are a subset of immutable types.
They are immutable types that reference only other `isbitstype` types or _primitive types_.
Primitive types are types whose data are a simple collection of bits.
A collection of primitive types [is defined by base](https://docs.julialang.org/en/v1/manual/types/#Primitive-Types).
The purpose of primitive types is to facilitate interoperability with LLVM.

## Case Study: Stack-Allocated Vectors (A.K.A. a Very Brief Introduction to StaticArrays.jl)

The usual `Vector{Float64}` is mutable, which means that it is heap allocated.
Let's see if we can create a more performant vector by creating a vector type that is allocated on the _stack_.

```julia
struct StackVector{N}
    data::NTuple{N, Float64}
end

StackVector(data::Vector{Float64}) = StackVector(Tuple(data))
```

Define `add` for the typical `Vector{Float64}` and our newly defined `StackVector`.

```julia
add(x::Vector{Float64}, y::Vector{Float64}) = x .+ y
add(x::StackVector{N}, y::StackVector{N}) where N = StackVector{N}(x.data .+ y.data)
```

Let's check that this works as intended.

```julia
julia> x = randn(10);

julia> y = randn(10);

julia> stack_x = StackVector(x);

julia> stack_y = StackVector(y);

julia> add(x, y)
10-element Vector{Float64}:
 -0.5453143850886275
  2.120385168072067
  1.1278328263047377
  1.6358682579762607
 -0.22486252827622277
 -2.1333012655133836
  2.6754332229859767
 -0.7701873679976846
  0.26775849165909
 -2.7389288669831786

julia> collect(add(stack_x, stack_y).data)
10-element Vector{Float64}:
 -0.5453143850886275
  2.120385168072067
  1.1278328263047377
  1.6358682579762607
 -0.22486252827622277
 -2.1333012655133836
  2.6754332229859767
 -0.7701873679976846
  0.26775849165909
 -2.7389288669831786
```

That looks good.
Now let's see what avoiding allocations on the heap gets us.

```julia
julia> using BenchmarkTools

julia> @benchmark z = add($x, $y)
BenchmarkTools.Trial:
  memory estimate:  160 bytes
  allocs estimate:  1
  --------------
  minimum time:     53.664 ns (0.00% GC)
  median time:      56.126 ns (0.00% GC)
  mean time:        59.544 ns (1.83% GC)
  maximum time:     572.958 ns (87.42% GC)
  --------------
  samples:          10000
  evals/sample:     987

julia> @benchmark stack_z = add($stack_x, $stack_y)
BenchmarkTools.Trial:
  memory estimate:  0 bytes
  allocs estimate:  0
  --------------
  minimum time:     0.052 ns (0.00% GC)
  median time:      0.055 ns (0.00% GC)
  mean time:        0.055 ns (0.00% GC)
  maximum time:     0.099 ns (0.00% GC)
  --------------
  samples:          10000
  evals/sample:     1000
```

Whoa!
What happened here is that the compiler is a little too clever:
it managed to figure out the answer at compile time and essentially hardcode the answer.
Compare this with

```julia
julia> @benchmark stack_z = $(add(stack_x, stack_y))
BenchmarkTools.Trial:
  memory estimate:  0 bytes
  allocs estimate:  0
  --------------
  minimum time:     0.052 ns (0.00% GC)
  median time:      0.055 ns (0.00% GC)
  mean time:        0.056 ns (0.00% GC)
  maximum time:     8.968 ns (0.00% GC)
  --------------
  samples:          10000
  evals/sample:     1000
```

To get around this issue, [BenchmarkTools.jl](https://github.com/JuliaCI/BenchmarkTools.jl#quick-start) advises the following trick:

```julia
julia> @benchmark stack_z = add($(Ref(stack_x))[], $(Ref(stack_y))[])
BenchmarkTools.Trial:
  memory estimate:  0 bytes
  allocs estimate:  0
  --------------
  minimum time:     2.276 ns (0.00% GC)
  median time:      2.293 ns (0.00% GC)
  mean time:        2.401 ns (0.00% GC)
  maximum time:     30.049 ns (0.00% GC)
  --------------
  samples:          10000
  evals/sample:     1000
```

That looks more reasonable.
For this small array, compared to the heap-allocated array, that's an 25x improvement in runtime!
This example demonstrates that memory allocations can substantially contribute to the total runtime of a program.

The idea of allocating vectors on the stack is certainly not mine.
Check out the fantastic [StaticArrays.jl](https://github.com/JuliaArrays/StaticArrays.jl), which provides a generic implementation of stack-allocated arrays.
If the size of the array is small, [these stack-allocated arrays can be significantly more performant than their heap-allocated counterparts](https://github.com/JuliaArrays/StaticArrays.jl#speed).
StaticArrays.jl works by automagically generating implementations of linear algebra operations that are optimised for specific sizes of vectors or matrices by using [generated functions](https://docs.julialang.org/en/v1/manual/metaprogramming/#Generated-functions).

## Garbage Collection

As more and more objects are allocated on the heap, eventually the heap fills up.
The purpose of the _garbage collector_ is to clean up the heap every once in a while.
The underlying principle of garbage collection is that objects are considered _garbage_, hence can be cleaned, if it can be proven that they cannot be _reached_ (used) anymore in future code.

Julia's garbage collector algorithm is called _mark and sweep_.
This algorithm consists of two phases:
the _mark phase_, where all objects that are _not_ garbage are found and marked so;
and the _sweep phase_, where all _unmarked_ objects are cleaned.
The mark phase first establishes a set of objects that are definitely _not_ garbage.
This set is called the _root set_, and [essentially consists of all global variables and everything on the stack](https://stackoverflow.com/questions/30080745/how-does-the-mark-in-mark-and-sweep-function-trace-out-the-set-of-objects-acce).
The garbage collector then follows everything that the root set references, and everything that those references reference, and marks those objects along the way.

During the sweep phase, the unmarked objects are _freed_, which simply means that it is internally recorded that their memory can be freely overwritten and used for something else.
These unmarked objects are found by walking through the whole heap.
Marked objects, on the other hand, remain untouched.
They are also not moved around:
you can imagine that the memory used by marked objects can sometimes be rearranged into a more compact arrangement.
This, however, takes time.
That Julia's garbage collector does not move marked objects around is referred to by saying that Julia's mark-and-sweep algorithm is _non-moving_ or _non-compacting_.

There is more fancy stuff going on.
For example, Julia's garbage collector is [_generational_](https://en.wikipedia.org/wiki/Tracing_garbage_collection#Generational_GC_(ephemeral_GC)).
You can check out the docstrings of [gc.c](https://github.com/JuliaLang/julia/blob/master/src/gc.c) for more details.
