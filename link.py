import os

links = {
    '/Users/wessel/Dropbox/Projects/Curriculum Vitae/cv.pdf': 'assets/cv.pdf',
    '/Users/wessel/Dropbox/Resources/Publications/My Publications/Lager, 2015, Beamforming in Sparse, Random, 3D Array Antennas with Fluctuating Element Locations.pdf': 'assets/conference/lager15.pdf',
    '/Users/wessel/Dropbox/Resources/Publications/My Publications/Bruinsma, 2016, Radiation Properties of Moving Constellations of Satellites.pdf': 'assets/conference/bruinsma16.pdf',
    '/Users/wessel/Dropbox/Resources/Publications/My Publications/Bosma, 2016, Grating Lobes Prediction in 3D Array Antennas.pdf': 'assets/conference/bosma17.pdf',
    '/Users/wessel/Dropbox/Resources/Publications/My Publications/Bruinsma, 2016, (Thesis) The Generalised Gaussian Process Convolution Model.pdf': 'assets/theses/bruinsma16.pdf',
    '/Users/wessel/Dropbox/Resources/Publications/My Publications/Bruinsma, 2015, (Thesis) An Extensible Toolkit For Real-Time High-Performance Wideband Spectrum Sensing.pdf': 'assets/theses/bruinsma15.pdf',
    '/Users/wessel/Dropbox/Resources/Publications/My Publications/Requeima, 2018, The Gaussian Process Autoregressive Regression Model (GPAR).pdf': 'assets/arxiv/requeima18.pdf',
    '/Users/wessel/Dropbox/Resources/Publications/My Publications/Bruinsma, 2018, Learning Causally-Generated Stationary Time Series.pdf': 'assets/arxiv/bruinsma18.pdf',
    '/Users/wessel/Dropbox/Projects/Documents/Presentations/Agreement/agreement.pdf': 'assets/talks/agreement.pdf',
    '/Users/wessel/Dropbox/Projects/Documents/Presentations/GPCM/gpcm.pdf': 'assets/talks/gpcm.pdf',
    '/Users/wessel/Dropbox/Projects/Documents/Presentations/InveniaCon, First/Reasoning About the World.pdf': 'assets/talks/reasoning-about-the-world.pdf',
    '/Users/wessel/Dropbox/Projects/Documents/Spike and Slab/spike-slab.pdf': 'assets/write-ups/spike-slab.pdf',
    '/Users/wessel/Dropbox/Projects/Documents/Agreement/agreement.pdf': 'assets/write-ups/agreement.pdf'
}

# Check that all sources exist.
for source, dest in links.items():
    if not os.path.exists(source):
        exit('Cannot find "{}".'.format(source))

# Make links.
for source, dest in links.items():
    # Remove `dest`.
    if os.path.exists(dest):
        os.unlink(dest)

    # Create directories.
    directory = os.path.dirname(dest)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Make link.
    os.link(source, dest)

print('Done.')