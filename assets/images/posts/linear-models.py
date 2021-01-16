#! python
from stheno import *
import numpy as np
import matplotlib.pyplot as plt
import wbml.plot


wbml.plot.tex()


B.set_random_seed(1)


class Figure:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        plt.figure()

    def __exit__(self, exc_type, exc_val, exc_tb):
        wbml.plot.tweak()
        path = f"linear-models-{self.name}.png"
        plt.savefig(path)
        plt.close()


prior = Measure()
x = np.linspace(0, 10, 100)

a = GP(1, measure=prior)
b = GP(10, measure=prior)
noise = GP(Delta(), measure=prior)


with Figure("constant-functions"):
    plt.plot(x, a(x).sample(20))


with Figure("slope-functions"):
    f = a * (lambda x: x)
    plt.plot(x, f(x).sample(20))


with Figure("linear-functions"):
    f = a * (lambda x: x) + b
    plt.plot(x, f(x).sample(20))


with Figure("noisy-linear-functions"):
    y = f + noise
    plt.plot(x, y(x).sample(20))


with Figure("noisy-linear-functions-2"):
    y = f + 0.5 * noise
    plt.plot(x, y(x).sample(20))


with Figure("observations"):
    x_obs = np.linspace(0, 10, 50_000)
    f_obs = 0.8 * x_obs - 2.5
    y_obs = f_obs + 0.5 * np.random.randn(50_000)
    plt.scatter(x_obs, y_obs, edgecolor="none", s=4, alpha=0.2, c="black")


post = prior | (y(x_obs), y_obs)
pred = post(f(x_obs))

print(repr(pred.mean))
print(repr(pred.var))

mean, lower, upper = pred.marginals()

print(repr(mean))
print(repr(upper - lower))

print(repr(f_obs - mean))
print(repr(np.mean((f_obs - mean) ** 2)))


with Figure("denoised-observations"):
    plt.scatter(x_obs, y_obs, edgecolor="none", s=4, alpha=0.2, c="black")
    plt.plot(x_obs, mean, c="tab:blue", lw=3)


def linear_model_denoise(x_obs, y_obs):
    prior = Measure()
    a = GP(1, measure=prior)            # Model for slope
    b = GP(10, measure=prior)           # Model for offset
    f = a * (lambda x: x) + b           # Noiseless linear model
    noise = GP(Delta(), measure=prior)  # Model for noise
    y = f + 0.5 * noise                 # Noisy linear model

    post = prior | (y(x_obs), y_obs)    # Condition on observations.
    pred = post(f(x_obs))               # Make predictions.
    return pred.marginals()             # Return the mean and associated error bounds.



print(repr(linear_model_denoise(x_obs, y_obs)))

import jax
import jax.numpy as jnp
import stheno.jax

try:
    linear_model_denoise_jitted = jax.jit(linear_model_denoise)
    print(linear_model_denoise(jnp.array(x_obs), jnp.array(y_obs)))
except Exception as e:
    print(e)

control_flow_cache = B.ControlFlowCache()
print(repr(control_flow_cache))
with control_flow_cache:
    linear_model_denoise(x_obs, y_obs)
print(repr(control_flow_cache))


@jax.jit
def linear_model_denoise_jitted(x_obs, y_obs):
    with control_flow_cache:
        return linear_model_denoise(x_obs, y_obs)


print(linear_model_denoise_jitted(jnp.array(x_obs), jnp.array(y_obs)))





