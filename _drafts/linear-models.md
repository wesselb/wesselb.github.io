---
layout:      post
title:       "Linear Models from a Gaussian Process Point of View with Stheno and JAX"
tags:        [python, machine learning]
comments:    true
---

## Introduction

A linear model prescribes a linear relationship between inputs and outputs.
Linear models are amongst the simplest of models; they are ubiquitous across science.
A linear model with Gaussian distributions on the coefficients forms one of the simplest instances of a _Gaussian process_.
In this post, we will give a brief introduction to linear models from a Gaussian process point of view.
We will see how a linear model can be implemented with Gaussian process probabilistic programming using [Stheno](https://github.com/wesselb/stheno), what the main computational challenges are, and how inference can be sped up using [JAX](https://github.com/google/jax).


## Linear Models from a Gaussian Process Point of View

Consider a data set $$(x_i, y_i)_{i=1}^n \subseteq \R \times \R$$ consisting of $$n$$ real-valued input--output pairs.
Suppose that we wish to estimate a linear relationship between the inputs and outputs:

$$ \label{eq:ax_b}
    y_i = a \cdot x_i + b + \e_i
$$

where $$a$$ is an unknown slope, $$b$$ is an unknown offset, and $$\e_i$$ is some error associated to the observation $$y_i$$.
To implement this model with Gaussian process probabilistic programming, we need to cast the problem in a _functional form_.
This means that we will assume that there is some underlying, random function $$y \colon \R \to \R$$ such that the observations are evaluations of this function: $$y_i = y(x_i)$$.
The model for the random function $$y$$ will embody the structure of the linear model \eqref{eq:ax_b}.
This may sound hard, but it is not difficult at all.
We let the random function $$y$$ be of the following form:

$$ \label{eq:ax_b_functional}
    y(x) = a(x) \cdot x + b(x) + \e(x)
$$

where $$a\colon \R \to \R$$ is a random _constant function_, $$b\colon \R \to \R$$ is also a random _constant function_, and $$\e\colon \R \to \R$$ is a random _noise function_.
Do you see the similarities between \eqref{eq:ax_b} and \eqref{eq:ax_b_functional}?
If that all doesn't fully make sense, don't worry;
things should become more clear as we implement the model.

To model random constant functions and random noise functions, we will use [Stheno](https://github.com/wesselb/stheno), which is a library for Gaussian process modelling.
In Stheno, a Gaussian process can be created with `GP(kernel)` where `kernel` is the the so-called _covariance function_ of the Gaussian process.
The kernel determines the properties of the function that the Gaussian process models.
For example, the kernel `EQ()` models smooth functions, and the kernel `Matern12()` models jaggedy functions.
See the [kernel cookbook](https://www.cs.toronto.edu/~duvenaud/cookbook/)  for an overview of commonly used kernels and the [documentation of Stheno](https://wesselb.github.io/stheno/docs/_build/html/readme.html#available-kernels) for the corresponding classes.
For constant functions, you can set the kernel to simply a constant, for example `1`, which then models the constant function with a Gaussian $$\Normal(0, 1)$$.
Let's start out by creating a Gaussian process for the random constant function $$a(x)$$ that models the slope.

```python
>>> from stheno import GP

>>> a = GP(1)

>>> a
GP(0, 1)
```

You can see how the Gaussian process looks like by sampling from it.
To sample from the Gaussian process `a`, evaluate it at some inputs `x`, `a(x)`, and call the method `sample`: `a(x).sample()`.
This shows that you can really think of a Gaussian process just like you think of a function:
pass it some inputs to get (the model for) the corresponding outputs.

```python
>>> x = np.linspace(0, 10, 100)

>>> plt.plot(x, a(x).sample(20)); plt.show()
```

{% include image.html
    name="Figure 1"
    ref="constant-functions"
    alt="Samples of a Gaussian process that models a constant function"
    src="posts/linear-models-constant-functions.png"
    width=400
%}

We've sampled a bunch of constant functions.
Sweet!
The next step in the model \eqref{eq:ax_b_functional} is to multiply the slope function $$a(x)$$ by $$x$$, where $$x$$ really is a shorthand for the identity function $$x \mapsto x$$:

```python
>>> f = a * (lambda x: x)

>>> f
GP(0, <lambda>)
```

This will give rise to functions like $$x \mapsto 0.1x$$ and $$x \mapsto -0.4x$$.

```python
>>> plt.plot(x, f(x).sample(20)); plt.show()
```

{% include image.html
    name="Figure 2"
    ref="slope-functions"
    alt="Samples of a Gaussian process that models functions with a random slope"
    src="posts/linear-models-slope-functions.png"
    width=400
%}

That is starting to look good!
The only ingredient that is missing is an offset.
We model the offset just like the slope, but here we set the kernel to `10` instead of `1`, which models the offset with a Gaussian $$\Normal(0, 10)$$.

```python
>>> b = GP(10)

>>> f = a * (lambda x: x) + b
AssertionError: Processes GP(0, <lambda>) and GP(0, 10 * 1) are associated to different measures.
```

Stheno has the abstraction called _measures_, where only `GP`s part of the same measure can be combined into new `GP`s;
the abstraction of measures it there to keep things safe and tidy.
What goes wrong here is that `a` and `b` are not part of the same measure.
Let's explicitly create a new measure and attach `a` and `b` to it.

```python
>>> from stheno import Measure

>>> prior = Measure()

>>> a = GP(1, measure=prior)

>>> b = GP(10, measure=prior)

>>> f = a * (lambda x: x) + b

>>> f
GP(0, <lambda> + 10 * 1)
```

Let's see how samples from `f` look like.

```python
>>> plt.plot(x, f(x).sample(20)); plt.show()
```

{% include image.html
    name="Figure 3"
    ref="linear-functions"
    alt="Samples of a Gaussian process that models linear functions"
    src="posts/linear-models-linear-functions.png"
    width=400
%}

Perfect!
We will use `f` as our linear model.

In practice, observations are corrupted with noise.
We can add some noise to lines in Figure [(3)](#figure-linear-functions) by adding a Gaussian process that models noise.
You can construct such a Gaussian process by using the kernel `Delta()`.

```python
>>> from stheno import Delta

>>> noise = GP(Delta(), measure=prior)

>>> y = f + noise

>>> y
GP(0, <lambda> + 10 * 1 + Delta())

>>> plt.plot(x, y(x).sample(20)); plt.show()
```

{% include image.html
    name="Figure 4"
    ref="noisy-linear-functions"
    alt="Samples of a Gaussian process that models noisy linear functions"
    src="posts/linear-models-noisy-linear-functions.png"
    width=400
%}

That looks more realistic.
But perhaps that's a bit too much noise.
We can tune down the amount of noise, for example, by scaling `noise` by `0.5`.

```python
>>> y = f + 0.5 * noise

>>> y
GP(0, <lambda> + 10 * 1 + 0.25 * Delta())

>>> plt.plot(x, y(x).sample(20)); plt.show()
```

{% include image.html
    name="Figure 5"
    ref="noisy-linear-functions-2"
    alt="Samples of a Gaussian process that models noisy linear functions"
    src="posts/linear-models-noisy-linear-functions-2.png"
    width=400
%}

Much better.

To summarise, our linear model is given by

```python
prior = Measure()

a = GP(1, measure=prior)            # Model for slope
b = GP(10, measure=prior)           # Model for offset
f = a * (lambda x: x) + b           # Noiseless linear model

noise = GP(Delta(), measure=prior)  # Model for noise
y = f + 0.5 * noise                 # Noisy linear model
```

We call a programme like this a _Gaussian process probabilistic programme_ (GPPP).
Let's sample some data from `y` that will make up an example data set $$(x_i, y_i)_{i=1}^n$$.

```python
>>> x_obs = np.linspace(0, 10, 50_000)

>>> y_obs = y(x_obs).sample()

>>> plt.scatter(x_obs, y_obs); plt.show()
```

{% include image.html
    name="Figure 6"
    ref="observations"
    alt="Some observations"
    src="posts/linear-models-observations.png"
    width=400
%}

We will see next how can we fit our model to this data.


## Inference in Linear Models

Suppose that we wish to remove the noise from the observations in Figure [(6)](#figure-observations).
We phrase this problem carefully in terms of our GPPP:
the observations `y_obs` are realisations of the _noisy_ linear model `y` at `x_obs`, _i.e._ realisations of `y(x_obs)`, and we wish to make predictions for the _noiseless_ linear model `f` at `x_obs`, _i.e._ predictions for `f(x_obs)`.

In Stheno, we can incorporate 


## Making Inference Fast

