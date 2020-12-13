---
layout:      post
title:       "Julia Learning Circle: Generated Functions"
tags:        [julia, julia learning circle, computer science]
comments:    true
---

In this post, we will take a brief look at [generated functions](https://docs.julialang.org/en/v1.6-dev/manual/metaprogramming/#Generated-functions).
Whereas a normal function outputs the result of the computation by the function, a generated function outputs _code that implements the function_.
In generating this code, the generated function can only make use of the _types_ of the arguments, not their _values_.
In a sense, generated functions offer ["on-demand code generation"](https://discourse.julialang.org/t/understanding-generated-functions/10092/4).
This mechanism is quite powerful and can be used when normal functions in combination with multiple dispatch cannot give you what you need.

To illustrate generated functions, we will build on the example of [stack-allocated vectors from the previous post]({% post_url 2020-11-23-julia-learning-circle-meeting-2 %}#case-study-stack-allocated-vectors-aka-a-very-brief-introduction-to-staticarraysjl), so first give that a quick look if you haven't yet.
In particular, we will extend our stack-allocated vector to a stack-allocated _matrix_ and we will use a generated function to implement matrix multiplication.
Let's start out by defining a stack-allocated vector and matrix.

```julia
struct StackMatrix{T, M, N, L}
    data::NTuple{L, T}
end

function StackVector(data::Vector{T}) where T
    return StackMatrix{T, length(data), 1, length(data)}(Tuple(data))
end
function StackMatrix(data::Matrix{T}) where T
    M, N = size(data)
    return StackMatrix{T, M, N, length(data)}(Tuple(data[:]))
end
```

The type signature is `StackMatrix{T, M, N, L}` where `T` is the type of the elements of the matrix, `M` is the number of rows of the matrix, `N` is the number of columns of the matrix, and `L = M * N` is the total number of elements in the matrix;
even though `L` can always be computed from `M` and `N`, we need `L` in the type signature, because it specifies the length of the `NTuple`.

Before we implement multiplication for general `StackMatrix{T, M, N, L}`s, we first implement the case of `StackMatrix{T, 2, 2, 4}`s.


```julia
import Base: *

function *(x::StackMatrix{T, 2, 2, 4}, y::StackMatrix{T, 2, 2, 4}) where T
    x11, x21, x12, x22 = x.data
    y11, y21, y12, y22 = y.data
    z11 = x11 * y11 + x12 * y21
    z21 = x21 * y11 + x22 * y21
    z12 = x11 * y12 + x12 * y22
    z22 = x21 * y12 + x22 * y22
    return StackMatrix{T, 2, 2, 4}((z11, z21, z12, z22))
end
```

Let's check that the implementation is correct.

```julia
julia> x = randn(2, 2);

julia> y = randn(2, 2);

julia> x_stack = StackMatrix(x);

julia> y_stack = StackMatrix(y);

julia> x * y
2×2 Matrix{Float64}:
 -1.16361    0.848159
  0.355827  -0.441428

julia> reshape(collect((x_stack * y_stack).data), 2, 2)
2×2 Matrix{Float64}:
 -1.16361    0.848159
  0.355827  -0.441428
```

Nice!
And it is quite a bit faster, too.

```julia
julia> @benchmark $x * $y
BenchmarkTools.Trial:
  memory estimate:  112 bytes
  allocs estimate:  1
  --------------
  minimum time:     54.112 ns (0.00% GC)
  median time:      59.993 ns (0.00% GC)
  mean time:        62.529 ns (1.27% GC)
  maximum time:     486.884 ns (83.35% GC)
  --------------
  samples:          10000
  evals/sample:     973

julia> @benchmark $(Ref(x_stack))[] * $(Ref(y_stack))[]
BenchmarkTools.Trial:
  memory estimate:  0 bytes
  allocs estimate:  0
  --------------
  minimum time:     3.015 ns (0.00% GC)
  median time:      3.033 ns (0.00% GC)
  mean time:        3.077 ns (0.00% GC)
  maximum time:     16.869 ns (0.00% GC)
  --------------
  samples:          10000
  evals/sample:     1000
```

The problem with multiplication of general `StackMatrix{T, M, N, L}`s is that the implementation depends on the particular values of `M` and `N` --- for example, the number of variables `z11`, `z21`, _et cetera_.
We will use a generated function to, for particular values of `M` and `N`, _automatically generate the implementation of the corresponding matrix multiplication_.
Generated functions are defined with the macro `@generated`.
The implementation of multiplication of general `StackMatrix{T, M, N, L}`s as follows:

```julia
import Base: *

@generated function *(
    x::StackMatrix{T, K, M, L₁},
    y::StackMatrix{T, M, N, L₂}
) where {T, K, M, N, L₁, L₂}
    # Unpack `x`.
    tuple_x = Expr(:tuple,  [Symbol("x_$(k)_$(m)") for m = 1:M for k = 1:K]...)
    unpack_x = :($tuple_x = x.data)

    # Unpack `y`.
    tuple_y = Expr(:tuple,  [Symbol("y_$(m)_$(n)") for n = 1:N for m = 1:M]...)
    unpack_y = :($tuple_y = y.data)

    # Perform multiplication.
    mults = Vector{Expr}()
    for k = 1:K, n = 1:N
        expr = Expr(
            :call,
            :+,
            [:($(Symbol("x_$(k)_$(m)")) * $(Symbol("y_$(m)_$(n)"))) for m = 1:M]...
        )
        push!(mults, :($(Symbol("z_$(k)_$(n)")) = $expr))
    end

    # Pack `z`.
    tuple_z = Expr(:tuple,  [Symbol("z_$(k)_$(n)") for n = 1:N for k = 1:K]...)
    pack_z = :(StackMatrix{T, K, N, L₃}($tuple_z))

    return Expr(
        :block,
        unpack_x,
        unpack_y,
        mults...,
        :(L₃ = K * N),
        :(return $pack_z)
    )
end
```

If we omit the macro `@generated`, we can call the implementation to inspect the generated code:

```julia
julia> x_stack * y_stack
quote
    (x_1_1, x_2_1, x_1_2, x_2_2) = x.data
    (y_1_1, y_2_1, y_1_2, y_2_2) = y.data
    z_1_1 = x_1_1 * y_1_1 + x_1_2 * y_2_1
    z_1_2 = x_1_1 * y_1_2 + x_1_2 * y_2_2
    z_2_1 = x_2_1 * y_1_1 + x_2_2 * y_2_1
    z_2_2 = x_2_1 * y_1_2 + x_2_2 * y_2_2
    L₃ = K * N
    return StackMatrix{T, K, N, L₃}((z_1_1, z_2_1, z_1_2, z_2_2))
end
```

Sweet!
This looks very much like our earlier implementation of the two-by-two case.
Let's double check that the implementation is indeed correct.

```julia
julia> x = randn(4, 2);

julia> y = randn(2, 3);

julia> x_stack = StackMatrix(x);

julia> y_stack = StackMatrix(y);

julia> x * y
4×3 Matrix{Float64}:
  0.125514  -0.0135978  -0.0283178
 -1.93756    0.450559    1.17303
  2.56769   -0.365378   -0.845966
  3.22549   -0.602203   -1.50065

julia> reshape(collect((x_stack * y_stack).data), 4, 3)
4×3 Matrix{Float64}:
  0.125514  -0.0135978  -0.0283178
 -1.93756    0.450559    1.17303
  2.56769   -0.365378   -0.845966
  3.22549   -0.602203   -1.50065
```

Like the two-by-two case, this implementation is quite a bit faster, too.

```julia
julia> @benchmark $x * $y
BenchmarkTools.Trial:
  memory estimate:  176 bytes
  allocs estimate:  1
  --------------
  minimum time:     205.100 ns (0.00% GC)
  median time:      219.162 ns (0.00% GC)
  mean time:        229.711 ns (0.74% GC)
  maximum time:     1.679 μs (75.82% GC)
  --------------
  samples:          10000
  evals/sample:     530

julia> @benchmark $(Ref(x_stack))[] * $(Ref(y_stack))[]
BenchmarkTools.Trial:
  memory estimate:  0 bytes
  allocs estimate:  0
  --------------
  minimum time:     15.097 ns (0.00% GC)
  median time:      15.665 ns (0.00% GC)
  mean time:        16.987 ns (0.00% GC)
  maximum time:     103.605 ns (0.00% GC)
  --------------
  samples:          10000
  evals/sample:     997
```