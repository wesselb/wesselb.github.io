import numpy as np
import matplotlib.pyplot as plt
from wbml.plot import tweak, pdfcrop
import lab as B
import pickle


with open('sawtooth/data.pickle', 'rb') as f:
    data = pickle.load(f)
with open('sawtooth/embedding.pickle', 'rb') as f:
    embedding = pickle.load(f)
with open('sawtooth/embedding_cnn.pickle', 'rb') as f:
    embedding_cnn = pickle.load(f)
with open('sawtooth/pred.pickle', 'rb') as f:
    pred = pickle.load(f)
with open('sawtooth/pred_convnp.pickle', 'rb') as f:
    pred_convnp = pickle.load(f)

plt.figure(figsize=(4.5, 1.5))
plt.scatter(data['xc'], data['yc'], style='train')
plt.xlim(-2, 2)
plt.ylim(-0.125, 1.125)
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
tweak(legend=False)

plt.savefig('sawtooth/data.pdf')
pdfcrop('sawtooth/data.pdf')

p1 = plt.plot(embedding['xz'], embedding['z1'], c='tab:blue', scaley=False)
p2 = plt.plot(embedding['xz'], embedding['z2'], c='tab:green', scaley=False)
plt.savefig('sawtooth/embedding.pdf')
pdfcrop('sawtooth/embedding.pdf')
for h in p1:
    h.remove()
for h in p2:
    h.remove()

p1 = plt.plot(embedding_cnn['xz'], embedding_cnn['z1'], c='tab:blue',
              scaley=False)
p2 = plt.plot(embedding_cnn['xz'], B.softplus(embedding_cnn['z2']),
              c='tab:green', scaley=False)
plt.savefig('sawtooth/embedding_cnn.pdf')
pdfcrop('sawtooth/embedding_cnn.pdf')
for h in p1:
    h.remove()
for h in p2:
    h.remove()

p1 = plt.plot(pred['xt'], pred['mu'], scaley=False, style='pred')
p2 = plt.fill_between(pred['xt'],
                      pred['mu'] - 2 * pred['std'],
                      pred['mu'] + 2 * pred['std'],
                      style='pred')
plt.savefig('sawtooth/pred.pdf')
pdfcrop('sawtooth/pred.pdf')
for h in p1:
    h.remove()
p2.remove()

plt.plot(pred_convnp['xt'], pred_convnp['samples'][:, :3],
         scaley=False, style='pred', ls='-', lw=.5)
plt.savefig('sawtooth/pred_convnp.pdf')
pdfcrop('sawtooth/pred_convnp.pdf')

plt.close()

# Make another, thinner plot.
plt.figure(figsize=(3, 1.5))
plt.scatter(data['xc'], data['yc'], style='train')
plt.xlim(-2, 2)
plt.ylim(-0.125, 1.125)
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
tweak(legend=False)

p1 = plt.plot(pred['xt'], pred['mu'], scaley=False, style='pred')
p2 = plt.fill_between(pred['xt'],
                      pred['mu'] - 2 * pred['std'],
                      pred['mu'] + 2 * pred['std'],
                      style='pred')
plt.savefig('sawtooth/pred_thin.pdf')
pdfcrop('sawtooth/pred_thin.pdf')
for h in p1:
    h.remove()
p2.remove()

plt.plot(pred_convnp['xt'], pred_convnp['samples'][:, :3],
         scaley=False, style='pred', ls='-', lw=.5)
plt.savefig('sawtooth/pred_convnp_thin.pdf')
pdfcrop('sawtooth/pred_convnp_thin.pdf')

plt.close()


# plt.savefig('sawtooth/embedding.pdf')
# pdfcrop('sawtooth/embedding.pdf')
