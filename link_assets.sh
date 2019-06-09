#!/usr/bin/env bash
ASSETS="/Users/wessel/Dropbox/Projects/wesselb.github.io/assets"
PRESENTATIONS="/Users/wessel/Dropbox/Projects/Documents/Presentations"
DOCUMENTS="/Users/wessel/Dropbox/Projects/Documents"
MYPUBS="/Users/wessel/Dropbox/Resources/Publications/My Publications"

# arXiv papers:
ln -f \
    "$MYPUBS/Bruinsma, 2018, Learning Causally-Generated Stationary Time Series.pdf" \
    "$ASSETS/arxiv/bruinsma18.pdf"

# Conference papers:
ln -f \
    "$MYPUBS/Lager, 2015, Beamforming in Sparse, Random, 3D Array Antennas with Fluctuating Element Locations.pdf" \
    "$ASSETS/conference/lager15.pdf"
ln -f \
    "$MYPUBS/Bruinsma, 2016, Radiation Properties of Moving Constellations of Satellites.pdf" \
    "$ASSETS/conference/bruinsma16.pdf"
ln -f \
    "$MYPUBS/Bosma, 2017, Grating Lobes Prediction in 3D Array Antennas.pdf" \
    "$ASSETS/conference/bosma17.pdf"
ln -f \
    "$MYPUBS/Requeima, 2019, The Gaussian Process Autoregressive Regression Model (GPAR).pdf" \
    "$ASSETS/conference/requeima19.pdf"

# Posters:
ln -f \
    "/Users/wessel/Dropbox/University Cambridge/Research/Documents/Stheno ProbProg Poster/main.pdf" \
    "$ASSETS/posters/probprog18.pdf"

# Talks:
ln -f \
    "$PRESENTATIONS/Agreement/agreement.pdf" \
    "$ASSETS/talks/agreement.pdf"
ln -f \
    "$PRESENTATIONS/GPCM/gpcm.pdf" \
    "$ASSETS/talks/gpcm.pdf"
ln -f \
    "$PRESENTATIONS/InveniaCon, First/reasoning_about_the_world.pdf" \
    "$ASSETS/talks/reasoning-about-the-world.pdf"
ln -f \
    "$PRESENTATIONS/Serum/serum.pdf" \
    "$ASSETS/talks/serum.pdf"
ln -f \
    "$PRESENTATIONS/CSSM/kernel_design.pdf" \
    "$ASSETS/talks/spectral-methods-kernel-design.pdf"
ln -f \
    "$PRESENTATIONS/CSSM/spectrum_estimation.pdf" \
    "$ASSETS/talks/spectral-methods-spectrum-estimation.pdf"
ln -f \
    "$PRESENTATIONS/CSSM/variational_inference.pdf" \
    "$ASSETS/talks/spectral-methods-variational-inference.pdf"
ln -f \
    "$PRESENTATIONS/OLMM/olmm-handout.pdf" \
    "$ASSETS/talks/orthogonal-bases-mogps.pdf"
    
# Theses:
ln -f \
    "$MYPUBS/Bruinsma, 2015, (Thesis) An Extensible Toolkit For Real-Time High-Performance Wideband Spectrum Sensing.pdf" \
    "$ASSETS/theses/bruinsma15.pdf"
ln -f \
    "$MYPUBS/Bruinsma, 2016, (Thesis) The Generalised Gaussian Process Convolution Model.pdf" \
    "$ASSETS/theses/bruinsma16.pdf"

# Write-ups:
ln -f \
    "$DOCUMENTS/Agreement/agreement.pdf" \
    "$ASSETS/write-ups/agreement.pdf"
ln -f \
    "$DOCUMENTS/Serum/serum.pdf" \
    "$ASSETS/write-ups/serum.pdf"
ln -f \
    "$DOCUMENTS/CSSM/main.pdf" \
    "$ASSETS/write-ups/spectral-methods.pdf"
ln -f \
    "$DOCUMENTS/Spike and Slab/spike_slab.pdf" \
    "$ASSETS/write-ups/spike-slab.pdf"

# CV:
ln -f \
    "/Users/wessel/Dropbox/Projects/Curriculum Vitae/cv.pdf" \
    "$ASSETS/cv.pdf"
