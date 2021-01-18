---
layout:      post
title:       "Finite Difference Methods"
tags:        [julia, python, numerics]
comments:    true
---

## Introduction

The derivative of a function $$f$$ at some point $$x$$ tells how a small change in $$x$$ translates to a change in $$f$$.[^1]
This piece of _local information_ finds many important applications.
For example, around any point $$x$$, one can construct the incredibly useful _Taylor expansion_ of $$f$$, which is a local, polynomial approximation of $$f$$ based on only its derivatives at $$x$$;
under certain conditions it is even possible to reconstruct $$f$$ entirely from all its derivatives at only that single point $$x$$---crazy!
Derivatives are also put into action in the field of optimisation:
to maximise $$f$$, a common strategy is to simply follow $$f$$ into its direction of steepest ascent, which---indeed---is given by $$f$$'s derivative. 
And optimisation is key to _many_ areas---think machine learning, economics and finance, and numerous disciplines of engineering.

Numerically computing derivatives is not always so straightforward.
For the function $$f$$ under consideration is often a complicated program, where the only thing we can do is query its output for a particular input.
In many cases, this complicated program is a composition of many elementary functions, which we _can_ differentiate;
repeated application of the chain rule using one of the many popular frameworks---[TensorFlow](https://tensorflow.org/), [PyTorch](https://pytorch.org/), or [Theano](http://deeplearning.net/software/theano/), to name a few---then computes the desired derivative, and this works excellently.
But it may happen that the derivative for a particular elementary function is not available, or that for your particular problem an _automatic differentation_ (AD) framework cannot be used at all.
It is therefore helpful to be able to _estimate_ derivatives numerically.
These estimators can always be computed, and are commonly used to verify derivatives computed by an AD framework.

Numerically estimating the derivative of a function $$f$$ at $$x$$ works by measuring how much $$f$$ changes if the input $$x$$ is slightly perturbed---the magnitude of the pertubation $$h$$ is called the _step size_.
Such estimators are called _finite difference methods_.
The big drawback of finite difference methods is that the step size $$h$$ must be chosen appropriately:
if $$h$$ is too big, then the estimate will poorly approximate the derivative; and if $$h$$ is too small, then the estimate will largely be dominated by numerical errors.
Choosing an adequate step size is a nontrivial matter.

This blog post serves as an introduction to the theory and practice of finite difference methods.
We will do so by discussing the usage and design of the simple Python and Julia package [FDM](https://github.com/wesselb/fdm)/[FDM.jl](https://github.com/invenia/fdm.jl).
FDM estimates derivatives of scalar functions with finite difference methods, and attempts to automatically determine an appropriate step size for you.

## Estimating Derivatives With FDM

FDM estimates $$f'(x)$$ by evaluating $$f$$ at a number of points nearby $$x$$---evaluating $$f$$ is called _sampling_ $$f$$ and the obtained values are called _samples_---and then appropriately weighting these samples to approximate $$f'(x)$$.
More precisely, if $$f$$ is sampled at some points $$(x_1,\ldots,x_n)$$, then the estimator for $$f'(x)$$ is of the form

$$ \label{eq:estimator}
    f'(x) \approx \frac{1}{h}\sum_{i=1}^n c_i f(x_i)
$$

where $$c=(c_1,\ldots, c_n)$$ are weights given to the samples, also referred to as the _coefficients_.
The sampling points $$(x_i)$$ are typically concentrated around $$x$$, and it is convenient to express them as $$x$$ plus a tiny bit:

$$ \label{eq:xi}
    x_i = x + h g_i.
$$

Here $$h$$ is the previously introduced step size, and $$g_i$$ determines how many step sizes $$x_i$$ is away from $$x$$.
Because the step size $$h$$ is the same for all sampling points $$x_i$$, a small $$h$$ will bring them close to $$x$$, whereas a large $$h$$ will make them more spread out.
In FDM, $$(g_1, \ldots, g_n)$$ are called _grid points_, collectively referred to as the _grid_.
[Figure 1](#figure-sampling) illustrates the sampling process for the grid $$g=(g_1,g_2)=(-1,1)$$.

{% include image.html
    name="Figure 1"
    ref="sampling"
    alt="Illustration of the sampling process in FDM"
    src="posts/fdm-sampling.png"
    width=400
%}

Substituting Equation \eqref{eq:xi} into Equation \eqref{eq:estimator}, the estimator for $$f'(x)$$ is of the form

$$
    f'(x) \approx \frac{1}{h} \sum_{i=1}^n c_i f(x + h g_i).
$$

For example, if $$c_1=1$$, $$c_2=-1$$, $$g_1=1$$, and $$g_2=0$$, then

$$
    f'(x) \approx \frac{f(x + h) - f(x)}{h}.
$$

This particular estimator is known as the _forward difference_ estimator.
We don't yet know whether this choice for the coefficients, grid, and step size is any good; we'll get to that later.

Let's consider an example, and try to construct a finite difference method `method` that evaluates $$f$$ on the grid `[-1, 1]`---like in [Figure 1](#sampling)---to estimate the first derivative of $$\sin(x)$$, $$\exp(x)$$, and $$x^2$$ at $$x=1$$.
To do so, we specify the grid and the order of the derivative to compute; FDM then computes the coefficients, and determinates an appropriate step size for us.

```python
>>> from fdm import FDM

>>> method = FDM(grid=[-1, 1], deriv=1)

>>> method.coefs
array([-0.5,  0.5])

>>> method.step
2.1073424255447017e-08

>>> method(np.sin, 1) - np.cos(1)
9.681416779372398e-10

>>> method(np.exp, 1) - np.exp(1)
7.867654083781872e-09

>>> method(lambda x: x ** 2, 1) - 2
2.64995003718127e-09
``` 

```julia
julia> using FDM

julia> method, report = fdm([-1, 1], 1; report=true)
(FDM.method, FDMReport:
  order of method:       2
  order of derivative:   1
  grid:                  [-1, 1]
  coefficients:          [-0.5, 0.5]
  roundoff error:        2.22e-16
  bounds on derivatives: 1.00e+00
  step size:             2.11e-08
  accuracy:              2.11e-08
)

julia> method(sin, 1) - cos(1)
9.681416779372398e-10

julia> method(exp, 1) - exp(1)
7.867654083781872e-9

julia> method(x -> x^2, 1) - 2
2.64995003718127e-9
```

We observe absolute error around $$10^{-9}$$.
Not bad.
But we're not restricted to such simple grids. 
We can choose larger, more complicated grids; larger grids means more samples of the function, which means more information about the function, which typically means a more accurate estimate.
Let's see.

```python
>>> method = FDM(grid=[-2, -1, 0, 1, 2], deriv=1)

>>> method.coefs
array([ 8.33333333e-02, -6.66666667e-01,  2.37904934e-16,  6.66666667e-01,
       -8.33333333e-02])

>>> method.step
0.0010842983568959566

>>> method(np.sin, 1) - np.cos(1)
-2.2315482794965646e-14

>>> method(np.exp, 1) - np.exp(1)
-2.1938006966593093e-13

>>> method(lambda x: x ** 2, 1) - 2
4.75175454539567e-14
```

```julia
julia> method, report = fdm([-2, -1, 0, 1, 2], 1; report=true)
(FDM.method, FDMReport:
  order of method:       5
  order of derivative:   1
  grid:                  [-2, -1, 0, 1, 2]
  coefficients:          [0.0833333, -0.666667, 0.0, 0.666667, -0.0833333]
  roundoff error:        2.22e-16
  bounds on derivatives: 1.00e+00
  step size:             1.08e-03
  accuracy:              3.84e-13
)

julia> method(sin, 1) - cos(1)
-1.247890679678676e-13

julia> method(exp, 1) - exp(1)
-1.4654943925052066e-14

julia> method(x -> x^2, 1) - 2
4.75175454539567e-14
```

And indeed, we have reduced the absolute error by 5 orders of magnitude.
Not bad at all.
Note that the step size now is on the order of $$10^{-3}$$, whereas that for the simpler grid was on the order of $$10^{-8}$$;
that's again 5 orders of magnitude difference, which shows that appropriate step sizes can vary greatly between finite difference methods.

In the next few sections we dive right into the theory that is behind all of this.
We first review how numbers are represented on a computer, and then see how derivatives can accurately be estimated simply by weighting samples.

## The Floating Point Representation of Numbers
That finite difference methods yield only an approximate answer is due to two sources of error: firstly, due to representing numbers on a computer with only finite accuracy; and secondly, due to the estimator being mathematically approximate, even in a world where numbers can be represented infinitely accurately.
An appropriately chosen step size carefully balances these two sources of error, and it is hence important to quantify the two, at least to some approximate degree.
In this section we review the way numbers are represented on a computer, and we derive an upper bound on the consequential error in a finite difference estimator.

Numbers on a computer are represented by the closest possible _floating point number_.
A floating point number is a number of the form

$$ \label{eq:fp-representation}
    (-1)^S \cdot (1 + F) \cdot 2^{E}
$$

where $$S \in \{0, 1\}$$ is called the _sign_, $$1 + F$$ the _mantissa_, $$F$$ the _fraction_, and $$E$$ the _exponent_.
The fraction $$F$$, as the name suggest, lies in $$[0, 1)$$, which is achieved by constructing $$F$$ from its bits $$F_1, F_2, F_3, \ldots $$ as follows:

$$
    F
    = F_1 \cdot 2^{-1} + F_2 \cdot 2^{-2} + F_3 \cdot 2^{-3} + \ldots
    = (0.F_1F_2F_3\cdots)_2
$$

where $$(x)_2$$ indicates that $$x$$ is denoted as a binary number.
The exponent $$E$$, on the other hand, is an integer centered around zero;
assuming that $$E$$ is stored using $$n$$ bits, this is achieved by subtracting $$2^{n-1} - 1$$ from its unsigned value.

Floating point numbers come in two precisions:
_single-precision_ floating point numbers---`np.float32`, for example---spend $$32$$ to store $$S$$, $$M$$, and $$E$$, whereas _double-precision_ floating point numbers---`np.float64`, for example---spend $$64$$ bits to do so.
[Table 1](#table-bits-allotment) shows a breakdown of the allotment of bits by the two formats.

{: #table-bits-allotment }
| Precision  | $$S$$ |  $$F$$ | $$E$$ | Total |
| - | :-: | :-: | :-: | :-: |
| Single | 1 bit | 23 bits | 8 bits | 32 bits |
| Double | 1 bit | 52 bits | 11 bits | 64 bits |

{% include table_caption.html
    name="Table 1"
    caption="Breakdown of the bits allotment of single-precision and double-precision floating point numbers"
%}

{% include image.html
    name="Figure 2"
    ref="fp-distribution"
    alt="Distribution of floating point numbers where the fraction is stored using 2 bits"
    src="posts/fdm-fps.png"
    width=800
%}

The discrepancy between a number and its approximate representation on a computer---the closest floating point number---is called the _round-off error_, which very much depends on how floating point numbers are distributed over the real line.
[Figure 2](#figure-fp-distribution) illustrates this distributed in the case that the fraction $$F$$ is stored using 2 bits.
We observe that floating point numbers get denser closer to zero, but can be far apart far away from zero, meaning that the round-off error is larger for bigger numbers.

Let $$x$$ be a real number, and denote by $$\fp(x)$$ the floating point number closest to $$x$$. 
[Figure 2](#figure-fp-distribution) further illustrates how a real number $$x$$ is rounded to the closest floating-point number $$\fp(x)$$.
The round-off error is quanitified by the _machine epsilon_ $$\e$$---also illustrated in [Figure 2](#figure-fp-distribution)---which gives an upper bound on the maximum relative error introduced by $$x \mapsto \fp(x)$$:

$$ \label{eq:machine-epsilon}
    \frac{|x - \fp(x)|}{|x|} \le  \e
    := \frac{1}{2}2^{-n}
$$

where $$n$$ is the number of bits used to store the fraction, 23 in the case of single precision and 52 in the case of double precision.
Note that if we do not assume that $$\fp(x)$$ is rounded appropriately, we find a machine epsilon $$\e$$ twice as large: $$\e = 2^{-n}$$.




Assuming that $$\e$$ is a power of two, which is not an unreasonable assumption given that numbers are stored in base $$2$$, this characterisation we can empirically determine the machine epsilon $$\e$$:

```python
>>> eps = 1.0

>>> while 1.0 != 1.0 + eps:
        eps /= 2.0

>>> eps
1.1102230246251565e-16

>>> 0.5 * 2 ** -52
1.1102230246251565e-16
```

```julia
julia> eps = 1.0
1.0

julia> while 1.0 != 1.0 + eps
           eps /= 2.0
       end

julia> eps
1.1102230246251565e-16

julia> 0.5 * 2^-52.0
1.1102230246251565e-16
```

Could compute float64 in similar manner, but that might 

upper bound on error.

In conclusion, the round-off error  the machine epsilon $$\e$$ quantifies the 

## Finite Difference Estimates of Derivatives
Quick recap, reference forward difference from section blah: reference

__Theorem (Taylor's).__
Let $$k \ge 1$$ be an integer, and let a function $$f\colon\R \to \R$$ be $$k$$ times differentiable at some $$a \in \R$$.
Then, for every $$x \in \R$$, there exists a $$\xi$$, strictly between $$x$$ and $$a$$, such that

$$
    f(x) = \sum_{i=1}^k \frac{f^{(i)}(a)}{i!}(x - a)^i + \frac{f^{(k+1)}(\xi)}{(k+1)!}(x - a)^{k+1}.
$$

__Proof.__
Bla.

cite: https://math.stackexchange.com/questions/481661/simplest-proof-of-taylors-theorem
$$\blacksquare$$

Order

Truncation error

Balance truncation error and roundoff error

## Cancellations of Step Sizes

Twitter trick

## Arbitrary Order Estimates on an Arbitrary Grid
Discuss what FDM does

Derivation

Implementation

## Testing Sensitivities in Reverse-Mode Automatic Differentiation Frameworks
2 issues: multi-input multi-output, approx num eq

Discuss issue with zero

Small cute proof

## So What's Next?
Richardson extrapolation

Automatic determination of `M`

Gradients, partial derivatives, and Hessians

## Conclusion
FDM simple package solely dedicated to. (solution)

Handy, don't have to choose step size: chosen automatically via balancing bla and bla.
Accuracy (gap)

Call for more: proposed future directions




[^1]: $$\ll \Delta x, \nabla f \rr \approx \Delta f$$, and the approximation becomes exact as $$\Delta x$$ becomes small.

[^2]: Interestingly enough, a decimal expansion of a number is not unique---$$1=0.999\cdots$$, for example---which is why both inequalities here have to be non-strict.

[^3]: Floating point numbers are not distributed evenly over the real line, so the choice of $$x$$ here matters. The choice $$x=1.5$$ works, because the distance between $$\fp(x)$$ and the previous and next floating point number are not anomalous. In constrast, $$x=1$$ might bring complications, because the distance between $$\fp(x)$$ and the previous floating point number is half that between $$\fp(x)$$ and the next.