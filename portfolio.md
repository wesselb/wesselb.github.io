---
layout:    static_page
permalink: /portfolio
title:     "Portfolio"
---

## Projects
<ul class="portfolio-list">
    {% include project_entry.html
        title="Stheno"
        link="https://github.com/wesselb/stheno"
        description="Gaussian process modelling in Python"
    %}
    {% include project_entry.html
        title="Plum"
        link="https://github.com/wesselb/plum"
        description="Multiple dispatch in Python"
    %}
    {% include project_entry.html
        title="LAB"
        link="https://github.com/wesselb/lab"
        description="A generic interface for linear algebra backends in Python"
    %}
    {% include project_entry.html
        title="FDM"
        link="https://github.com/wesselb/fdm"
        description="Estimate derivatives with finite differences in Python"
    %}
    {% include project_entry.html
        title="FDM.jl"
        link="https://github.com/invenia/FDM.jl"
        description="Estimate derivatives with finite differences in Julia"
    %}
    {% include project_entry.html
        title="Varz"
        link="https://github.com/wesselb/varz"
        description="Painless variables in PyTorch and TensorFlow"
    %}
    {% include project_entry.html
        title="Gaussian Process Autoregressive Regression Model"
        link="https://github.com/wesselb/gpar"
        description="Implementation of GPAR in Python"
    %}
    {% include project_entry.html
        title="Causal Gaussian Process Convolution Model"
        link="https://github.com/wesselb/cgpcm"
        description="Implementation of the CGPCM in Python"
    %}
    {% include project_entry.html
        title="WBML"
        link="https://github.com/wesselb/WBML"
        description="A collection of machine learning algorithms"
    %}
    {% include project_entry.html
        title="Catalogue"
        link="https://github.com/wesselb/catalogue"
        description="Resource management with Alfred"
    %}
    {% include project_entry.html
        title="wesselb.github.io"
        link="https://github.com/wesselb/wesselb.github.io"
        description="This website"
    %}
</ul>

## arXiv Submissions
<ul class="portfolio-list">
    {% include publication_entry.html
        file="arxiv/bruinsma18.pdf"
        authors="Bruinsma, W. P. and Turner, R. E."
        year="2018"
        title="Learning Causally Generated Stationary Time Series"
        note="arXiv:1802.08167"
    %}
</ul>

## Publications
<ul class="portfolio-list">
    {% include publication_entry.html
        file="conference/requeima19.pdf"
        authors="Requeima, J., Tebbutt W. C., Bruinsma, W. P., and Turner R. E."
        year="2019"
        title="The Gaussian Process Autoregressive Model (GPAR)"
        note="Artificial Intelligence and Statistics (AISTATS), 22nd International Conference on"
    %}
    {% include publication_entry.html
        file="conference/bosma17.pdf"
        authors="Bosma, S., Bruinsma, W. P., Hes, R. P., Bentum, M. J., and Lager, I. E."
        year="2017"
        title="Grating Lobe Prediction in 3D Array Antennas"
        note="Antennas and Propagation (EuCAP), 11th European Conference on"
    %}
    {% include publication_entry.html
        file="conference/bruinsma16.pdf"
        authors="Bruinsma, W. P., Hes, R. P., Bosma, S., Lager, I. E., and Bentum, M. J."
        year="2016"
        title="Radiation Properties of Moving Constellations of (Nano) Satellites: A Complexity Study"
        note="Antennas and Propagation (EuCAP), 10th European Conference on"
    %}
    {% include publication_entry.html
        file="conference/lager15.pdf"
        authors="Bentum, M. J., Lager, I. E., Bosma, S., Bruinsma, W. P., and Hes, R. P."
        year="2015"
        title="Beamforming in Sparse, Random, 3D Array Antennas with Fluctuating Element Locations"
        note="Antennas and Propagation (EuCAP), 9th European Conference on"
    %}
</ul>

## Posters
<ul class="portfolio-list">
    {% include publication_entry.html
        file="posters/probprog18.pdf"
        authors="Tebbutt, W. C., Bruinsma, W. P., and Turner R. E."
        title="Gaussian Process Probabilistic Programming"
        year="2018"
        note="Probabilistic Programming (ProbProg), The International Conference on"
    %}
</ul>

## Theses
<ul class="portfolio-list">
    {% include publication_entry.html
        file="theses/bruinsma16.pdf"
        authors="Bruinsma, W. P."
        year="2016"
        title="The Generalised Gaussian Process Convolution Model"
        note="Department of Engineering, University of Cambridge. Thesis for the degree Master of Philosophy."
    %}
    {% include publication_entry.html
        file="theses/bruinsma15.pdf"
        authors="Bruinsma, W. P., Hes, R. P., Kroep, H. J. C., Leliveld, T. C., Melching, W. M., and aan de Wiel, T. A."
        year="2015"
        title="An Extensible Toolkit for Real-Time High-Performance Wideband Spectrum Sensing"
        note="Faculty of Electrical Engineering, Mathematics and Computer Science, Delft University of Technology. Thesis for the degree Bachelor of Science."
    %}
</ul>

## Talks
<ul class="portfolio-list">
    {% include publication_entry.html
        file="talks/spectral-methods-spectrum-estimation.pdf"
        authors="Requeima J. R., and Bruinsma, W. P."
        title="Spectral Methods in Gaussian Modelling: Spectrum Estimation"
    %}
    {% include publication_entry.html
        file="talks/spectral-methods-variational-inference.pdf"
        authors="Requeima J. R., and Bruinsma, W. P."
        title="Spectral Methods in Gaussian Modelling: Variational Inference"
    %}
    {% include publication_entry.html
        file="talks/spectral-methods-kernel-design.pdf"
        authors="Requeima J. R., and Bruinsma, W. P."
        title="Spectral Methods in Gaussian Modelling: Kernel Design"
    %}
    {% include publication_entry.html
        file="talks/serum.pdf"
        authors="Bruinsma, W. P."
        title="A Bayesian Truth Serum"
    %}
    {% include publication_entry.html
        file="talks/agreement.pdf"
        authors="Bruinsma, W. P."
        title="Agreeing to Disagree"
    %}
    {% include publication_entry.html
        file="talks/gpcm.pdf"
        authors="Bruinsma, W. P."
        title="The Gaussian Process Convolution Model"
    %}
    {% include publication_entry.html
        file="talks/reasoning-about-the-world.pdf"
        authors="Bruinsma, W. P."
        title="Reasoning About the World"
    %}
</ul>

## Write-Ups
<ul class="portfolio-list">
    {% include publication_entry.html
        file="write-ups/spectral-methods.pdf"
        authors="Requeima J. R., and Bruinsma W. P."
        title="Spectral Methods in Gaussian Modelling"
    %}
    {% include publication_entry.html
        file="write-ups/serum.pdf"
        authors="Bruinsma, W. P."
        title="A Bayesian Truth Serum"
    %}
    {% include publication_entry.html
        file="write-ups/spike-slab.pdf"
        authors="Bruinsma, W. P."
        title="Spike and Slab Priors"
    %}
    {% include publication_entry.html
        file="write-ups/agreement.pdf"
        authors="Bruinsma, W. P."
        title="Agreeing to Disagree"
    %}
</ul>