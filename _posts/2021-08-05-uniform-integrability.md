---
layout:      post
title:       "A Short Note on Uniform Integrability"
tags:        [probability theory, math]
comments:    true
---

## Introduction

A sequence of random variables $(X_n)_{n \ge 1} \sub L^1$ is called $L^1$-convergent if there exists some limit $X \in L^1$ such that $\E\|X_n - X\| \to 0$ as $n \to \infty$.
In this post, we briefly discuss a necessary and sufficient condition for $L^1$-convergence called *uniform integrability*.

## Uniform Integrability

**Definition.** A collection of random variables $\mathcal{F}$ is called *uniformly integrable* if

\begin{equation}
    \lim_{K \to \infty} \sup\,\\\{ \E[\ind_{|X| \ge K} |X|] : X \in \mathcal{F} \\\} = 0.
\end{equation}

Noting that $\E[\ind_{\abs{X} \ge K} \abs{X}] = \E\abs{X - \ind_{\abs{X} < K} X}$, this condition can also be written as

\begin{equation}
    \lim_{K \to \infty} \sup\,\\\{ \E\abs{X - \ind_{\abs{X} < K} X} : X \in \mathcal{F} \\\} = 0.
\end{equation}

In other words, if $\mathcal{F}$ is uniformly integrable, then you can choose a single value of $K > 0$ such that, uniformly over $X \in \mathcal{F}$, the random variable $\ind_{\abs{X} < K} X$ is a good approximation of $X$ in terms of the $L^1$-norm.
Crucially, every $\ind_{\abs{X} < K} X$ is a bounded random variable, which is often a desirable property.
Therefore, you could aptly call a family which is uniform integrable a family which allows a *uniform bounded approximation*.

But what about the name *uniform integrability*?
For a single variable $X$, it is true that
\begin{equation}
    \E\abs{X} < \infty
    \iff
    \lim_{K \to \infty} \E[\ind_{|X| \ge K} |X|] = 0.
\end{equation}
Hence, you could call a family of random variables *uniformly* integrable if the limit on the RHS, which is equivalent to integrability, converges uniformly over the family.

The bounded approximation given by uniform integrability can be made a bit nicer.
Instead of bounding $X$ by applying the function $f_K(x) = \ind_{\abs{x} < K} x$, which exhibits a discontinuity at $\abs{x} = K$, uniform integrability allows us to bound $X$ by applying the nicer function $g_K(x) = \max(\min(x, K), -K)$, which is a fully continuous function:
\begin{equation}
    \E\abs{g_K(X) - X}
    = \E[\ind_{\abs{X} \ge K}\abs{\abs{X} - K}]
    \le \E[\ind_{\abs{X} \ge K}\abs{X}] + \E[\ind_{\abs{X} \ge K} K]
    \le 2 \E[\ind_{\abs{X} \ge K} \abs{X}],
\end{equation}
which uniformly converges to zero as $K \to \infty$.
Henceforth, for any random variable $X$, denote by $X^K =\max(\min(X, K), -K)$ the *trunction of $X$ at level $K$*.
Since $g_K$ is continuous, trunctions in this way preserves limits.

Finally, to check that a family of random variables is uniformly integrable, the following two facts are very useful:

1. If $\sup\,\\\{ \E[\abs{X}^{p}] : X \in \mathcal{F}\\\} < \infty$ for some $p  > 1$, then $\mathcal{F}$ is uniformly integrable.

2. Every family $\\\{ \E[X \cond \mathcal{G}] : \mathcal{G} \text{ is a sub-}\sigma\text{-algebra}\\\}$ is uniformly integrable.

## A Necessary and Sufficient Condition for $L^1$-Convergence

A standard way to prove that a sequence of random variables $(X_n)_{n \ge 1}$ is $L^1$-convergent to some limit is to use *bounded convergence*, an instance of the dominated convergence theorem.
Recall that a sequence of random variables $(X_n)\_{n \ge 1}$ is called *convergent in probability* if there exists a limit $X$ such that $\P(\abs{X - X_n} \ge \e) \to 0$ for every $\e > 0$.

**Theorem (bounded convergence).**
If $(X_n)\_{n \ge 1}$ and $X$ are bounded by some $K > 0$ and $X_n \to X$ in probability, then $X_n \to X$ in $L^1$.

**Proof.**
Without loss of generality, assume that $X = 0$, so it remains to demonstrate that $\E\abs{X_n} \to 0$.
Let $\e > 0$.
Using the assumption that $\abs{X_n} \le K$, the idea is to consider the cases $\abs{X_n} \in [0, \e]$ and $\abs{X_n} \in (\e, K]$:

\begin{equation}
    \E\abs{X_n}
    = \E[\abs{X_n} \ind_{\abs{X_n} \in [0, \e]}] + \E[\abs{X_n} \ind_{\abs{X_n} \in (\e, K]}]
    \le \e + K\, \E[\ind_{\abs{X_n} \in (\e, K]}]
    \le \e + K\, \P(\abs{X_n} \ge \e).
\end{equation}

Using that assumpion that $\P(\abs{X_n} \ge \e) \to 0$ as $n \to \infty$, hence $\limsup_{n \to \infty} \E\abs{X_n} \le \e$.
Since $\e > 0$ was arbitrary, this proves that $\lim_{n \to \infty} \E\abs{X_n}=0$. {% include qed.html %}

Bounded convergence is an incredibly useful tool, but the assumption that $(X_n)\_{n \ge 1}$ and $X$ are bounded can be too strong.
A looser assumption is that $(X_n)\_{n \ge 1}$ and $X$ uniformly allow a *bounded approximation*, *i.e.* that $(X_n)\_{n \ge 1}$ (and therefore the union of $(X_n)\_{n \ge 1}$ and $X$) are *uniformly integrable*.
This looser condition turns out to not just be sufficient but also necessary.

**Theorem (Vitali's).**
Let $(X_n)\_{n \ge 1}$ be a sequence of random variables and let $X$ be a random variable.
Then (a) $(X_n)\_{n \ge 1} \sub L^1$, $X \in L^1$, and $X_n \to X$ in $L^1$ if and only if (b) $(X_n)\_{n \ge 1} \sub L^1$ is uniformly integrable and $X_n \to X$ in probability.

**Proof.**
We only show the hard direction, which is that (b) implies (a).
Assume that $(X_n)\_{n \ge 1} \sub L^1$ is uniformly integrable and $X_n \to X$ in probability.
To begin with, it is true[^1] that $X \in L^1$.
Since $X \in L^1$, $(X_n - X)_{n \ge 1}$ is uniformly integrable and $X_n - X \to 0$ in probability in any case, so without loss of generality assume that $X = 0$.

Uniform integrability gives a uniform bounded approximation of the sequence:

\begin{equation} \label{eq:uniform-approx}
    \lim_{K \to \infty} \sup_{n \ge 1}\, \E\abs{X_n - \ind_{\abs{X_n} < K} X_n} = 0.
\end{equation}

For every $K>0$, the sequence $(\ind\_{\abs{X_n} < K} X\_n)_{n \ge 1}$ is bounded and $\ind\_{\abs{X_n} < K} X_n \to 0$ in probability, so $\ind\_{\abs{X_n} < K} X_n \to 0$ in $L^1$ by bounded convergence.
The idea is to then take $K \to \infty$ to show that also $X_n \to 0$ in $L^1$.
To wit, by the triangle inequality,

\begin{equation}
    \limsup_{n \to \infty} \E\abs{X_n}
    \le \sup_{n \ge 1}\, \E\abs{X_n - \ind_{\abs{X_n} < K} X_n} + \limsup_{n \to \infty} \E\abs{\ind_{\abs{X_n} < K} X_n}
    \overset{\text{(i)}}{=} \sup_{n \ge 1}\, \E\abs{X_n - \ind_{\abs{X_n} < K} X_n}
\end{equation}

where (i) follows from that $\ind\_{\abs{X_n} < K} X_n \to 0$ in $L^1$ by bounded convergence.
Taking $K \to \infty$ and using \eqref{eq:uniform-approx} then shows the result.
{% include qed.html %}

## Application: Strengthening of Convergence in Distribution

A sequence of random variables $(X_n)\_{n \ge 1}$ is called *weakly convergent* if there exists a limit $X$ such that, for every $f \colon \R \to \R$ continuous and bounded, it is true that $\E[f(X_n)] \to \E[f(X)]$.
A limitation of weak convergence is that it only handles *bounded* $f$;
for example, weak convergence does not imply that $\E[X_n] \to \E[X]$.
As we illustrate now, the assumption of uniform integrability can be used to strengthen the conclusion of weak convergence to include $\E[X_n] \to \E[X]$.

The key observation is as follows: if $(X_n)\_{n \ge 1}$ and $X$ were bounded by some $K > 0$, then we can apply the truncation function $g_K$, which is a continuous and bounded function, to conclude that
\begin{equation}
    \E[X_n] = \E[g_K(X_n)] \to \E[g_K(X)] = \E[X].
\end{equation}
Instead of assuming boundedness, now assume that $(X_n)\_{n \ge 1}$ is only uniformly integrable.
For all $K > 0$, consider the uniform bounded approximations $(X^K_n)\_{n \ge 1}$ and $X^K$.
Because the trunction operation is continuous, every $(X_n^K)\_{n \ge 1}$ is still weakly convergent to $X^K$.
Morever, $(X_n^K)\_{n \ge 1}$ and $X^K$ are bounded by $K > 0$.
The foregoing argument then shows that
$
    \lim_{n \to \infty} \E[X_n^K] = \E[X^K].
$
Therefore,
\begin{equation}
    \lim_{n \to \infty} \E[X_n]
    = \lim_{n \to \infty} \lim_{K \to \infty} \E[X_n^K]
    = \lim_{K \to \infty} \lim_{n \to \infty} \E[X_n^K]
    = \lim_{K \to \infty} \E[X^K]
    = \E[X],
\end{equation}
where the interchange of limits is allowed by uniformity of the bounded approximation.


## Summary

A family of random variables is called *uniformly integrable* if it allows a *uniform bounded approximation*.
Allowing a uniform bounded approximation turns out to be the right characterisation of $L^1$-convergence:
a sequence is $L^1$-convergent if and only if it is uniformly integrable.
Uniformly integrability is generally useful tool:
if you can prove a result for bounded random variables, then you might be able to prove the result for the greater class of uniformly integrable random variables by considering a uniform bounded approximation.

Thanks to [Jiri Hron](https://sites.google.com/view/jirihron) for helpful comments on a draft of this post.

[^1]:
    Since $X_n \to X$ in probability, $X_{n_k} \to X$ almost surely along some subsequence $(X_{n_k})_{k \ge 0}$.
    Therefore, using Fatou's lemma,

    \begin{equation}
        \E\abs{X}
            = \E[\lim_{k \to \infty} \abs{X_{n_k}}]
            \le \liminf_{k \to \infty} \E[\abs{X_{n_k}}]
            < \infty,
    \end{equation}

    where the right hand side is bounded because any uniformly integrable family is uniformly bounded in $L^1$.
