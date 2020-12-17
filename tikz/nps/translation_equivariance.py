from stheno import GP, Matern52
import matplotlib.pyplot as plt
from wbml.plot import tweak, pdfcrop
import numpy as np


f = GP(Matern52())
x = np.linspace(0, 6, 100)

x_obs = np.array([0.5, 1.5, 3.5])
y_obs = f(x_obs).sample().flatten()
x_obs_shifted = x_obs + 2

mean, lower, upper = (f | (x_obs, y_obs))(x).marginals()
mean_shifted, lower_shifted, upper_shifted = \
     (f | (x_obs_shifted, y_obs))(x).marginals()


plt.figure(figsize=(2.5, 1.25))
plt.scatter(x_obs, y_obs, style='train', s=15)
plt.ylim(lower.min() - 0.1, upper.max() + 0.1)
plt.xlim(x.min(), x.max())
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
tweak(legend=False)

plt.savefig(f'translation_equivariance/data.pdf')
pdfcrop(f'translation_equivariance/data.pdf')

plt.plot(x, mean, style='pred')
plt.fill_between(x, lower, upper, style='pred')

plt.savefig(f'translation_equivariance/pred.pdf')
pdfcrop(f'translation_equivariance/pred.pdf')

plt.close()

plt.figure(figsize=(2.5, 1.25))
plt.scatter(x_obs_shifted, y_obs, style='train', s=15)
plt.ylim(lower_shifted.min() - 0.1, upper_shifted.max() + 0.1)
plt.xlim(x.min(), x.max())
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
tweak(legend=False)

plt.savefig(f'translation_equivariance/data_shifted.pdf')
pdfcrop(f'translation_equivariance/data_shifted.pdf')

plt.plot(x, mean_shifted, style='pred')
plt.fill_between(x, lower_shifted, upper_shifted, style='pred')

plt.savefig(f'translation_equivariance/pred_shifted.pdf')
pdfcrop(f'translation_equivariance/pred_shifted.pdf')




