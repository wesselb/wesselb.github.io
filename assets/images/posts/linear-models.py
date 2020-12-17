from stheno import *
import numpy as np
import matplotlib.pyplot as plt
import wbml.plot


wbml.plot.tex()


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


model = Measure()
x = np.linspace(0, 10, 100)

a = GP(1, measure=model)
b = GP(10, measure=model)
noise = GP(Delta(), measure=model)


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
    y_obs = y(x_obs).sample()
    plt.scatter(x_obs, y_obs, edgecolor="none", s=4, alpha=0.2, c="black")



