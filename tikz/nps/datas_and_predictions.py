from stheno import GP, Matern52
import matplotlib.pyplot as plt
import matplotlib
from wbml.plot import tweak, pdfcrop
import numpy as np


np.random.seed(8)

x = np.linspace(0, 6, 100)

f = GP(Matern52())

prefix = ['', '', '\\tilde']
context_label = ['^{(c)}_1', '^{(c)}_n', '']
target_label = ['^{(t)}_1', '^{(t)}_n', '']

for i in range(3):
    n_obs = np.random.randint(3, 5 + 1)
    x_obs = np.random.rand(n_obs) * x.max()
    y_obs = f(x_obs).sample().flatten()

    mean, lower, upper = (f | (x_obs, y_obs))(x).marginals()

    n_test = np.random.randint(3, 5 + 1)
    x_test = np.random.rand(n_test) * x.max()
    y_test = (f | (x_obs, y_obs))(x_test).sample().flatten()

    plt.figure(figsize=(2.5, 1.25))
    plt.scatter(x_obs, y_obs, style='train', s=15,
                label=f'${prefix[i]} D{context_label[i]}$')
    plt.ylim(lower.min() - 0.1, upper.max() + 0.1)
    plt.xlim(x.min(), x.max())
    plt.gca().set_xticklabels([])
    plt.gca().set_yticklabels([])
    matplotlib.rc('legend', fontsize=8)
    tweak(legend=True)

    plt.savefig(f'datas_and_predictions/data{i + 1}.pdf')
    pdfcrop(f'datas_and_predictions/data{i + 1}.pdf')

    plt.plot(x, mean, style='pred')
    plt.fill_between(x, lower, upper, style='pred')

    plt.savefig(f'datas_and_predictions/pred{i + 1}.pdf')
    pdfcrop(f'datas_and_predictions/pred{i + 1}.pdf')

    plt.scatter(x_test, y_test, style='test', s=15,
                label=f'${prefix[i]} D{target_label[i]}$')
    tweak(legend=True)
    plt.savefig(f'datas_and_predictions/test{i + 1}.pdf')
    pdfcrop(f'datas_and_predictions/test{i + 1}.pdf')




