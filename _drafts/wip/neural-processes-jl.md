---
layout:      post
title:       "NeuralProcesses.jl"
tags:        [julia, machine learning]
comments:    true
---

{% include image.html
   url="https://github.com/wesselb/ConvCNPs.jl/raw/master/loop.gif"
%}

## Introduction

[(Conditional)](https://arxiv.org/abs/1807.01613) [Neural Processes](https://arxiv.org/abs/1807.01622) ((C)NPs) are a flexible and rich class of models that parametrise a predictive distribution through an encoding of observed data.
Their flexibility enables them to be deployed in a myriad of applications, such as image completion, image generation, time series prediction, and spatio-temporal modelling.
Neural Processes have seen much interest over the recent years, resulting in the addition of several new well-performing members to the Neural Process family.
As an effort to accelerate the development and evaluation of NP architectures, we present [NeuralProcesses.jl](https://github.com/wesselb/NeuralProcesses.jl), a framework for NPs built on top of [Flux.jl](https://github.com/FluxML/Flux.jl).
NeuralProcesses.jl provides basic building blocks that can be flexibly composed, mixed, and matched to reconstruct many NP architectures from the literature, or even expand to architectures not yet considered.

A recently introduced member of the Neural Process family called the [Convolutional Conditional Neural Process](https://openreview.net/forum?id=Skey4eBYPS) (ConvCNP) proposes to account for _translation equivariance_ in the data: if the observations are shifted, then the predictions should be shifted accordingly.
Translation equivariance is an important inductive bias for many learning problems, such as the aforementioned applications.
The ConvCNP has been demonstrated to achieve state-of-the-art performance on several established NP benchmarks.

In this post, we give a brief introduction to meta-learning, the Neural Process Family, and NeuralProcesses.jl.
To demonstrate the key concepts of the package, we walk through an implementation of the ConvCNP.
We will then use the ConvCNP to predict a sawtooth wave, an otherwise challenging task due to the wave's discontinuous nature.
We conclude with a brief demonstration of how the building blocks of NeuralProcess.jl can be used to construct several prominent NP architectures.

## Meta-Learning

For prediction tasks where data is scarce, it is crucial to learn from other tasks with similar statistical structure.
Namely, there could be important features or statistical subtleties that are not apparent from a single task, but these features may reveal themselves when considering many tasks at once.
This setting, where one has access to many tasks with similar statistical structure, is the setting of _meta-learning_.

The setting of meta-learning is different from the usual setting for supervised learning.
In supervised learning, we have a single data set $$D = D^{(c)} \cup D^{(t)}$$ comprising a _context set_ $$D^{(c)}$$, a collection of input--output pairs $$(x^{(c)}_i, y^{(c)}_i)_{i=1}^n$$ corresponding to observed data points; and a _target set_ $$D^{(t)}$$, a collection of input--output pairs $$(x^{(t)}_i, y^{(t)}_i)_{i=1}^m$$ corresponding to data points that we do not observe, but wish to make predictions for.

{% include image.html
   name="Figure 1"
   ref="meta-learning"
   width="600"
   alt="Illustation of meta-learning"
   src="posts/nps-meta-learning.png"
%}

In meta-learning, we have access to a collection of data sets $$(D_i)_{i=1}^n$$ corresponding to tasks with similar statistical structure, and we aim to best learn a procedure that makes predictions for a collection of new tasks $$(\tilde D_i)_{i=1}^m$$ that share this statistical structure.
In the _meta-training phase_, we use $$(D_i)_{i=1}^m$$ as examples to learn how to best exploit the statistical structure across the tasks; and in the _meta-test phase_, we apply our learned procedure to make predictions for the context sets in $$(\tilde D_i)_{i=1}^m$$.

The learned procedure can be viewed as a map

$$
    \phi_\theta\colon \mathcal{D} \to \mathcal{P}
$$

from the space $$\mathcal{D}$$ of all data sets to the space $$\mathcal{P}$$ of all distributions, where the map $$\phi_\theta$$ depends on some parameters $$\theta \in \Theta$$.
For a context set $$D^{(c)}$$, the distribution $$\phi_\theta(D^{(c)})$$ is the prediction for the corresponding target set $$D^{(t)}$$.
Denote the density of $$\phi_\theta(D^{(c)})$$ by $$p_\theta(D^{(t)} \cond D^{(c)})$$.
Note that this is abuse of notation:
For slightly subtle reasons, $$p_\theta(D^{(t)} \cond D^{(c)})$$ need not be a posterior distribution in the sense that it can be obtained through Bayes' rule, even though the notation suggests so.

During the meta-train phase, we compare $$\phi(D^{(c)}_i)$$ with $$D^{(t)}_i$$ for all $$D_i$$ in $$(D_i)_{i=1}^n$$ to best tune the parameters $$\theta$$ of our procedure; and during the meta-test phase, we use $$\phi_\theta(\tilde D^{(c)}_i)$$ as the prediction for $$\tilde D^{(t)}_i$$ for all $$\tilde D_i$$ in $$(\tilde D_i)_{i=1}^m$$.
The meta-train phase is often performed using maximum likelihood estimation:

$$
    \theta^* = \argmax_{\theta} \prod_{i=1}^n p_\theta(D^{(t)}_i \cond D^{(c)}_i).
$$

The meta-train phase, the meta-test phase, and the map $$\phi$$ are illustrated in Figure [(1)](#figure-meta-learning).
Although Figure [(1)](#figure-meta-learning) illustrates 1D regression examples, this formulation of meta-learning is quite general and applies to more complicated data sets and tasks.

One example of meta-learning is _few-shot learning_: there are many classes with only a few examples (_shots_) per class, and we wish to classify a new, yet unobserved class given, again, only a few examples for that class. 
Another example is _sim-to-real transfer_: we use a simulator to generate many synthetic data sets, and aim to exploit the statistical structure in these to make predictions for real-world data, which is often limited.

## Conditional Neural Processes

Neural Processes are a powerful family of probabilistic models that are particular parametrisations of the map $$\phi$$. 
The [Conditional Neural Process](https://arxiv.org/abs/1807.01613) is, in a sense, the simplest such parametrisation.
The CNP uses neural networks to directly parametrise the mean and variance of $$p_\theta(D^{(t)} \cond D^{(c)})$$:

$$
    p_\theta(D^{(t)} \cond D^{(c)})
    = p_\theta((y^{(t)}_i)_{i=1}^m \, | \, (x^{(t)}_i)_{i=1}^m, \, D^{(c)})
    = \prod_{i=1}^m \mathcal{N}(y^{(t)}_i|\, \mu_\theta(x^{(t)}_i, D^{(c)}), \sigma^2_\theta(x^{(t)}_i, D^{(c)}))
$$

where

$$ \label{eq:mean_var_cnp_definition}
    \mu_\theta\colon \mathcal{X} \times \mathcal{D} \to \mathbb{R}
    \quad \text{and} \quad
    \sigma^2_\theta\colon \mathcal{X} \times \mathcal{D} \to (0, \infty)
$$

are neural networks, parametrised by $$\theta$$, that map a target input $$x^{(t)} \in \mathcal{X}$$ and the context set $$D^{(c)}$$ to respectively the mean and variance of the prediction for the corresponding target output $$y^{(t)}$$.

Equation \eqref{eq:mean_var_cnp_definition} states that $$\mu_\theta$$ and $$\sigma^2_\theta$$ are functions on the space of all data sets $$\mathcal{D}$$.
This may seem innocent at a first glance.
Not quite.
Conventional neural networks take in arrays as inputs.
However, $$\mu_\theta$$ and $$\sigma^2_\theta$$ must take in a _collection of input--output pairs of variable size_.
Moreover, a data set _does not depend on the order of the data set_, so neither should $$\mu_\theta$$ and $$\sigma^2_\theta$$.
How do we design such neural networks?

The answer to this design problem is provided by [Zaheer et al. (2017)](https://arxiv.org/abs/1703.06114), who propose the Deep Set architecture:

$$ \label{eq:rho-sum-phi}
    \mu_\theta(x^{(t)}, D^{(c)})
    = \rho_\theta\parens{
        x^{(t)},
        r
    }
    \quad \text{where} \quad
    r = \sum_{(x^{(c)}, y^{(c)}) \in D^{(c)}} \psi_\theta(x^{(c)}, y^{(c)})
$$

where $$\psi_\theta\colon \mathcal{X} \times \mathcal{Y} \to \R^d$$ is neural network called the _encoder_ and $$\rho_\theta\colon \mathcal{X} \times \R^d \to \R$$ is another neural network called the _decoder_.
The parameterisation for the variance $$\sigma_\theta^2$$ is similar, but also ensures positivity.
In this architecture, $$r$$ can be thought of as the _representation_ of the context set $$D^{(c)}$$.
The summation really is the clever part:
it works for context sets $$D^{(c)}$$ of variable size --- the number of elements in the sum simply changes --- and, because addition is commmutative, the representation $$r$$ does not depend on the order of the data set.
We thus see that Equation \eqref{eq:rho-sum-phi} achieves the design desiderata.

## Convolutional Conditional Neural Processes

The main problem with Conditional Neural Processes is that they are a little too wild:
they need to train on enormous amounts of data for a long time to perform well, which means that they are not very parameter efficient, and their generalisation capabilities prove poor empirically.
To alleviate these two key issues, parameter inefficiency and poor generalisation, we impose more structure on the architectures of $$\rho_\theta$$ and $$\psi_\theta$$.

{% include image.html
   name="Figure 2"
   ref="translation-equivariance"
   width="500"
   alt="Illustation of translation equivariance"
   src="posts/nps-translation-equivariance.png"
%}

The [Convolutional Conditional Neural Process](https://openreview.net/forum?id=Skey4eBYPS) --- the member of the Neural Process family that we focus on in the post --- proposes to account for a symmetry called _translation equivariance_ in the data: if the observations are shifted, then the predictions should be shifted accordingly.
Translation equivariance is illustrated in Figure [(2)](#translation-equivariance).

To incorporate translation equivariance in the model, [Gordon et al. (2020)](https://openreview.net/forum?id=Skey4eBYPS) modify $$\mu_\theta$$ and $$\sigma^2_\theta$$ and propose the Set Convolution architecture:

$$ \label{eq:set-conv}
    \mu_\theta(x^{(t)}, D^{(c)})
    = \rho_\theta(r)(x^{(t)})
    \quad \text{where} \quad
    r = x \mapsto \sum_{(x^{(c)}, y^{(c)}) \in D^{(c)}}
        \begin{bmatrix} 1  \\ y^{(c)} \end{bmatrix}
        k_\theta(x -  x^{(c)})
$$

where --- it becomes a little technical now --- $$k_\theta$$ is a [positive-definite kernel](https://en.wikipedia.org/wiki/Positive-definite_kernel) [associated to](https://en.wikipedia.org/wiki/Reproducing_kernel_Hilbert_space#Moore%E2%80%93Aronszajn_theorem) a [Reproducing Kernel Hilbert Space (RKHS)](https://en.wikipedia.org/wiki/Reproducing_kernel_Hilbert_space) $$\mathcal{H}$$ and $$\rho_\theta\colon \mathcal{H}^2 \to C_b(\R)$$ is a continuous, _translation-equivariant_ transformation of functions mapping from the RKHS $$\mathcal{H}$$ to the space of continuous, bounded functions $$C_b(\R)$$, which is then evaluated at $$x^{(t)}$$.

In Equation \eqref{eq:set-conv}, the representation $$r$$ is a _function_, which is infinite and hence cannot be stored on a computer.
In practice, we evaluate $$r$$ on a prespecified grid, called the _discretisation_.
Moreover, $$\rho_\theta$$ is a map between two abstract functions spaces, which cannot be implemented on a computer.
In practice, we exploit the requirement that $$\rho_\theta$$ must be translation equivariant, which allows us to approximate it with a convolutional neural network (CNN); this is where the model owes it name from.
The ability to use CNNs instead of multi-layer perceptrons (MLPs) is a _huge_ win, because CNNs are vastly more parameter efficient.

Equation \eqref{eq:set-conv} perhaps remains a little unintuitive.
We will see its working in a practical example next.

## NeuralProcesses.jl

The implementation of Neural Processes is generally involved and requires several building blocks.
One main ... neural processes consist of a so-called encoder and decoder. In fact, the implementations of many neural processes are very similar and only differ in their details.

This is the motivation behind NeuralProcesses.jl, where we have attempted to identify the basic building blocks that make up neural processes. These building blocks can then be mixed and matched to easily reconstruct many existing architectures from the literature, and even expand to novel architectures not yet considered.

As mentioned on the previous slide, a neural process consists of an encoder and a decoder. Consider a data set, e.g. the collection of three input–output pairs depicted in the scatter plot. The encoder takes in the data and transforms it into some abstract representation r. The decoder then takes in this representation, and transforms it into a prediction over the input domain, which we can evaluate at any test inputs.

For the implementation of encoder–decoder architectures, it is convenient if the three objects — the data, encoding, and prediction — have a common representation. The key insight is that the data can be viewed as a function, mapping training inputs to the corresponding training outputs. The prediction is also a function, mapping test inputs to a prediction for the corresponding test outputs. These predictions could be means and variances, but they can also be more general. In NeuralProcesses.jl, everything is represented as a function, which means that the encoding and decoding operations, which we will collectively call coding, become transformations of functions. This is the fundamental abstraction upon which the package is built.

## Implementation of the ConvCNP with NeuralProcesses.jl

Pseudo-code for core components 

```julia
test(x) = x
```

GIF: training for fixed context set

Juicy details:
- depthwise separable convs
- receptive field
- empty-set
- leaky RELU's

## Example: Predicting a Sawtooth Function

We will have many time series with shared structure---for example, many sawtooth waves with varying frequency, amplitude, and offset---and aim to make predictions for a new similar, but unobserved time series.

Consider a 1D example; see paper for image experiments

GIF: sequential inference

## Conclusion




To train a neural process, we consider many small data sets, split every one of them into a train and test set, and optimise the likelihoods of the test sets under the predictions. Then, at test time, once a neural process is trained, to obtain a prediction for a data set that we have not seen before, we can simply apply the mapping.

The power of neural processes is that, at test time, they are able to produce fast, probabilistic predictions for unseen data.

Although the slides illustrate 1D regression examples, this formulation of meta-learning is quite general and applies to more complicated data sets and tasks.

The member of the Neural Process family that was first published is the Conditional Neural Process by Marta Garnelo and colleagues in 2018, which they followed up with the Neural Process in the same year. After that came the Attentive Neural Process, and many others followed. The difference between Conditional Neural Processes and Neural Processes is that the conditional models can only produce marginal predictive statistics — e.g. means and variances — whilst the unconditional models are able to produce coherent predictive sample paths.

To give you a taste of what neural processes can do, consider the following picture tweeted by a famous celebrity where only 5% of the pixels are kept. The Convolutional Conditional Neural Process is able to reconstruct the original picture pretty accurately, though the result is not perfect.

The implementation of neural processes can be involved and require several building blocks. However, as the figure illustrates, all neural processes consist of a so-called encoder and decoder. In fact, the implementations of many neural processes are very similar and only differ in their details.

This is the motivation behind NeuralProcesses.jl, where we have attempted to identify the basic building blocks that make up neural processes. These building blocks can then be mixed and matched to easily reconstruct many existing architectures from the literature, and even expand to novel architectures not yet considered.

As mentioned on the previous slide, a neural process consists of an encoder and a decoder. Consider a data set, e.g. the collection of three input–output pairs depicted in the scatter plot. The encoder takes in the data and transforms it into some abstract representation r. The decoder then takes in this representation, and transforms it into a prediction over the input domain, which we can evaluate at any test inputs.

For the implementation of encoder–decoder architectures, it is convenient if the three objects — the data, encoding, and prediction — have a common representation. The key insight is that the data can be viewed as a function, mapping training inputs to the corresponding training outputs. The prediction is also a function, mapping test inputs to a prediction for the corresponding test outputs. These predictions could be means and variances, but they can also be more general. In NeuralProcesses.jl, everything is represented as a function, which means that the encoding and decoding operations, which we will collectively call coding, become transformations of functions. This is the fundamental abstraction upon which the package is built.
Slide 5
Let’s illustrate the package by implementing the Convolutional Conditional Neural Process, which is a particular instance of a Conditional Neural Process that incorporates a symmetry called translation equivariance.

Consider a data set and the prediction for that data set. If we shift the data set by a certain amount, then translation equivariance states that the corresponding prediction should be equal to the original prediction shifted by the same amount.

Translation equivariance enables the Convolutional Conditional Neural Process, or ConvCNP in short, to leverage the parameter efficiency of convolutional neural networks, which we will implement using Flux.jl.

Consider the data set depicted in the scatter plot. This data set is generated by a sawtooth wave. We will illustrate how a trained ConvCNP can be used to infer the underlying sawtooth.

We first implement the encoder. The ConvCNP uses a fancy encoder that maps into a function space. We cannot exactly represent the resulting function, so, as an approximation, we represent a discretisation of the function instead. The encoder of the ConvCNP is a so-called set convolution, which directly maps the data set to the discretised functional representation. Moreover, the ConvCNP produces a deterministic encoding. We will later see what happens when we produce a stochastic encoding instead. If we run this code — note that the plots depict the actual output of the code — we obtain the following encoding, which consists of two functions.

The decoder takes in these functions and first transforms them with a CNN. Observe that we can already see sawtooth-like patterns emerging. The decoder then passes the result to another set convolution, which maps back from the function space of the encoding to the space of the data. The decoder finally produces predictive means and variances.

Putting together the encoder and decoder, we obtain the following prediction for the data, which nicely recovers the underlying sawtooth.

A problem of the ConvCNP is that it only produces predictive means and variances; it is not able to produce coherent predictive sample paths. To remedy this, we can instead use a stochastic encoding by simply — and this is the only change — swapping out the Deterministic() for another CNN and HeterogeneousGaussian(). The resulting model is called the Convolutional Neural Process, ‘which recently appeared on arXiv. The Convolutional Neural Process is able to produce nice looking sample paths that interpolate the data.

NeuralProcesses.jl consists of basic building blocks that can be put together in different ways to give rise to a wide variety of models. For example, this is the original Neural Process, which consists of three encoders in parallel, where two are deterministic and one is stochastic. The types Chain, which is from Flux, and Parallel are used to flexibly glue things together. For any model that you come up with, inference and learning are automatic.

As a final example of what the package can do, we could modify the Neural Process by swapping out the deterministic MLP encoder for an attentive mechanism. The resulting model is called the Attentive Neural Process.

Thank you for listening.

