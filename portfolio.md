---
layout:    static_page
permalink: /portfolio
title:     "Portfolio"
---

## Machine Learning Projects
<ul class="portfolio-list">
    {% include project_entry.html
        title="Stheno"
        link="https://github.com/wesselb/stheno"
        description="Gaussian process modelling in Python"
    %}
    {% include project_entry.html
        title="Gaussian Process Autoregressive Regression Model"
        link="https://github.com/wesselb/gpar"
        description="Implementation of GPAR in Python"
    %}
    {% include project_entry.html
        title="Orthogonal Linear Mixing Model"
        link="https://github.com/wesselb/olmm"
        description="Implementation of the OLMM in Python"
    %}
    {% include project_entry.html
        title="GPAR-OLMM"
        link="https://github.com/wesselb/gpar-olmm"
        description="Implementation of GPAR-OLMM in Python"
    %}
    {% include project_entry.html
        title="Convolutional Conditional Neural Processes"
        link="https://github.com/cambridge-mlg/convcnp"
        description="Implementation of ConvCNP in Python"
    %}
</ul>

## Projects
<ul class="portfolio-list">
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
        description="Painless optimisation of constrained convariables in PyTorch, and TensorFlow, and AutoGrad"
    %}
    {% include project_entry.html
        title="Matrix"
        link="https://github.com/wesselb/matrix"
        description="Structured matrices in Python"
    %}
    {% include project_entry.html
        title="Algebra"
        link="https://github.com/wesselb/algebra"
        description="Algebraic structures in Python"
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

## Publications
<ul class="portfolio-list">
    {% include publication_entry.html
        file="publications/Gordon, 2020, Convolutional Conditional Neural Processes.pdf"
        authors="Gordon, J., Bruinsma W. P., Foong, A. Y. K., Requeima, J., Dubois Y., and Turner R. E."
        year="2020"
        title="Convolutional Conditional Neural Processes"
        note="International Conference on Learning Representations (ICLR), 8th"
    %}
    {% include publication_entry.html
        file="publications/Berkovich, 2019, GP-ALPS, Automatic Latent Process Selection for Multi-Output Gaussian Process Models.pdf"
        authors="Berkovich B., Perim, E., and Bruinsma, W. P."
        year="2019"
        title="GP-ALPS: Automatic Latent Process Selection for Multi-Output Gaussian Process Models"
        note="Advanced in Approximate Bayesian Inference (AABI), 2nd Symposium on"
    %}
    {% include publication_entry.html
        file="publications/Requeima, 2019, The Gaussian Process Autoregressive Regression Model (GPAR).pdf"
        authors="Requeima, J., Tebbutt W. C., Bruinsma, W. P., and Turner R. E."
        year="2019"
        title="The Gaussian Process Autoregressive Model (GPAR)"
        note="Artificial Intelligence and Statistics (AISTATS), 22nd International Conference on"
    %}
    {% include publication_entry.html
        file="publications/Bosma, 2017, Grating Lobes Prediction in 3D Array Antennas.pdf"
        authors="Bosma, S., Bruinsma, W. P., Hes, R. P., Bentum, M. J., and Lager, I. E."
        year="2017"
        title="Grating Lobe Prediction in 3D Array Antennas"
        note="Antennas and Propagation (EuCAP), 11th European Conference on"
    %}
    {% include publication_entry.html
        file="publications/Bruinsma, 2016, Radiation Properties of Moving Constellations of Satellites.pdf"
        authors="Bruinsma, W. P., Hes, R. P., Bosma, S., Lager, I. E., and Bentum, M. J."
        year="2016"
        title="Radiation Properties of Moving Constellations of (Nano) Satellites: A Complexity Study"
        note="Antennas and Propagation (EuCAP), 10th European Conference on"
    %}
    {% include publication_entry.html
        file="publications/Lager, 2015, Beamforming in Sparse, Random, 3D Array Antennas with Fluctuating Element Locations.pdf"
        authors="Bentum, M. J., Lager, I. E., Bosma, S., Bruinsma, W. P., and Hes, R. P."
        year="2015"
        title="Beamforming in Sparse, Random, 3D Array Antennas with Fluctuating Element Locations"
        note="Antennas and Propagation (EuCAP), 9th European Conference on"
    %}
</ul>

## arXiv Submissions
<ul class="portfolio-list">
    {% include publication_entry.html
        file="arxiv/Bruinsma, 2019, Scalable Exact Inference in Multi-Output Gaussian Processes.pdf"
        authors="Bruinsma, W. P., Perim, E., Tebbutt, W., Hosking, J. S., Solin, A., and Turner, R. E."
        year="2019"
        title="Exact Scalable Inference in Multi-Output Gaussian Processes"
        note="arXiv:1911.06287"
    %}
    {% include publication_entry.html
        file="arxiv/Bruinsma, 2018, Learning Causally-Generated Stationary Time Series.pdf"
        authors="Bruinsma, W. P. and Turner, R. E."
        year="2018"
        title="Learning Causally Generated Stationary Time Series"
        note="arXiv:1802.08167"
    %}
</ul>

## Posters
<ul class="portfolio-list">
    {% include publication_entry.html
        file="posters/Tebbutt, 2019, (Poster) Gaussian Process Probabilistic Programming.pdf"
        authors="Tebbutt, W. C., Bruinsma, W. P., and Turner R. E."
        title="Gaussian Process Probabilistic Programming"
        year="2018"
        note="Probabilistic Programming (ProbProg), The International Conference on"
    %}
</ul>

## Theses
<ul class="portfolio-list">
    {% include publication_entry.html
        file="theses/Bruinsma, 2016, (Thesis) The Generalised Gaussian Process Convolution Model.pdf"
        authors="Bruinsma, W. P."
        year="2016"
        title="The Generalised Gaussian Process Convolution Model"
        note="Department of Engineering, University of Cambridge. Thesis for the degree Master of Philosophy."
    %}
    {% include publication_entry.html
        file="theses/Bruinsma, 2015, (Thesis) An Extensible Toolkit For Real-Time High-Performance Wideband Spectrum Sensing.pdf"
        authors="Bruinsma, W. P., Hes, R. P., Kroep, H. J. C., Leliveld, T. C., Melching, W. M., and aan de Wiel, T. A."
        year="2015"
        title="An Extensible Toolkit for Real-Time High-Performance Wideband Spectrum Sensing"
        note="Faculty of Electrical Engineering, Mathematics and Computer Science, Delft University of Technology. Thesis for the degree Bachelor of Science."
    %}
</ul>

## Talks
<ul class="portfolio-list">
    {% include publication_entry.html
        file="talks/Bruinsma, Orthogonal Bases for Multi-Output Gaussian Processes (Handout).pdf"
        authors="Bruinsma, W. P."
        title="Orthogonal Bases for Multi-Output Gaussian Processes"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, Topic 4, Spectrum Estimation.pdf"
        authors="Requeima J. R., and Bruinsma, W. P."
        title="Spectral Methods in Gaussian Modelling: Spectrum Estimation"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, Topic 3, Variational Inference.pdf"
        authors="Requeima J. R., and Bruinsma, W. P."
        title="Spectral Methods in Gaussian Modelling: Variational Inference"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, Topic 2, Kernel Design.pdf"
        authors="Requeima J. R., and Bruinsma, W. P."
        title="Spectral Methods in Gaussian Modelling: Kernel Design"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, A Bayesian Truth Serum.pdf"
        authors="Bruinsma, W. P."
        title="A Bayesian Truth Serum"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, Agreeing to Disagree.pdf"
        authors="Bruinsma, W. P."
        title="Agreeing to Disagree"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, GPCM.pdf"
        authors="Bruinsma, W. P."
        title="The Gaussian Process Convolution Model"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, Reasoning About The World.pdf"
        authors="Bruinsma, W. P."
        title="Reasoning About the World"
    %}
</ul>

## Write-Ups
<ul class="portfolio-list">
    {% include publication_entry.html
        file="write-ups/Requeima, Spectral Methods in Gaussian Modelling.pdf"
        authors="Requeima J. R., and Bruinsma W. P."
        title="Spectral Methods in Gaussian Modelling"
    %}
    {% include publication_entry.html
        file="write-ups/Bruinsma, A Bayesian Truth Serum.pdf"
        authors="Bruinsma, W. P."
        title="A Bayesian Truth Serum"
    %}
    {% include publication_entry.html
        file="write-ups/Bruinsma, Spike and Slab Priors.pdf"
        authors="Bruinsma, W. P."
        title="Spike and Slab Priors"
    %}
    {% include publication_entry.html
        file="write-ups/Bruinsma, Agreeing to Disagree.pdf"
        authors="Bruinsma, W. P."
        title="Agreeing to Disagree"
    %}
</ul>