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
        badge_stars="wesselb/stheno"
    %}
    {% include project_entry.html
        title="Gaussian Process Autoregressive Regression Model"
        link="https://github.com/wesselb/gpar"
        description="Implementation of GPAR in Python"
        badge_stars="wesselb/gpar"
    %}
    {% include project_entry.html
        title="Neural Processes"
        link="https://github.com/wesselb/NeuralProcesses.jl"
        description="A framework for composing Neural Processes in Julia"
        badge_stars="wesselb/NeuralProcesses.jl"
    %}
    {% include project_entry.html
        title="Convolutional Conditional Neural Processes"
        link="https://github.com/cambridge-mlg/convcnp"
        description="Implementation of the ConvCNP in Python"
        badge_stars="cambridge-mlg/convcnp"
    %}
    {% include project_entry.html
        title="Gaussian Process Convolution Model"
        link="https://github.com/wesselb/gpcm"
        description="Implementation of several variants of the GPCM in Python"
        badge_stars="wesselb/gpcm"
    %}
    {% include project_entry.html
        title="Orthogonal Instantatenous Linear Mixing Model"
        link="https://github.com/wesselb/oilmm"
        description="Implementation of the OILMM in Python"
        badge_stars="wesselb/oilmm"
    %}
    {% include project_entry.html
        title="GPAR-OILMM"
        link="https://github.com/wesselb/gpar-olmm"
        description="Implementation of GPAR-OILMM in Python"
        badge_stars="wesselb/gpar-olmm"
    %}
</ul>

## Projects
<ul class="portfolio-list">
    {% include project_entry.html
        title="Plum"
        link="https://github.com/wesselb/plum"
        description="Multiple dispatch in Python"
        badge_stars="wesselb/plum"
    %}
    {% include project_entry.html
        title="LAB"
        link="https://github.com/wesselb/lab"
        description="A generic interface for linear algebra backends in Python"
        badge_stars="wesselb/lab"
    %}
    {% include project_entry.html
        title="FDM"
        link="https://github.com/wesselb/fdm"
        description="Estimate derivatives with finite differences in Python"
        badge_stars="wesselb/fdm"
    %}
    {% include project_entry.html
        title="FiniteDifferences.jl"
        link="https://github.com/JuliaDiff/FiniteDifferences.jl"
        description="Estimate derivatives with finite differences in Julia"
        badge_stars="JuliaDiff/FiniteDifferences.jl"
    %}
    {% include project_entry.html
        title="Varz"
        link="https://github.com/wesselb/varz"
        description="Painless optimisation of constrained convariables in PyTorch, TensorFlow, AutoGrad, and JAX"
        badge_stars="wesselb/varz"
    %}
    {% include project_entry.html
        title="Matrix"
        link="https://github.com/wesselb/matrix"
        description="Structured matrices in Python"
        badge_stars="wesselb/matrix"
    %}
    {% include project_entry.html
        title="Algebra"
        link="https://github.com/wesselb/algebra"
        description="Algebraic structures in Python"
        badge_stars="wesselb/algebra"
    %}
    {% include project_entry.html
        title="WBML"
        link="https://github.com/wesselb/wbml"
        description="A collection of machine learning algorithms"
        badge_stars="wesselb/wbml"
    %}
    {% include project_entry.html
        title="Note"
        link="https://github.com/wesselb/note"
        description="Simple and quick note taking system"
        badge_stars="wesselb/note"
    %}
    {% include project_entry.html
        title="Catalogue"
        link="https://github.com/wesselb/catalogue"
        description="Resource management with Alfred"
        badge_stars="wesselb/catalogue"
    %}
    {% include project_entry.html
        title="wesselb.github.io"
        link="https://github.com/wesselb/wesselb.github.io"
        description="This website"
        badge_stars="wesselb/wesselb.github.io"
    %}
</ul>

## Publications
<ul class="portfolio-list">
    {% include publication_entry.html
        file="publications/Bruinsma, 2021, The Gaussian Neural Process.pdf"
        authors="Bruinsma W. P., Requeima J., Foong, A. Y. K., Gordon. J., and Turner R. E."
        year="2021"
        title="The Gaussian Neural Process"
        note="Advances in Approximate Bayesian Inference (AABI), 3rd Symposium on"
    %}
    {% include publication_entry.html
        file="publications/Xia, 2021, The Gaussian Process Latent Autoregressive Model.pdf"
        authors="Xia, R., Bruinsma W. P., Tebbutt W., and Turner R. E."
        year="2021"
        title="The Gaussian Process Latent Autoregressive Model"
        note="Advances in Approximate Bayesian Inference (AABI), 3rd Symposium on"
    %}
    {% include publication_entry.html
        file="publications/Foong, 2020, Meta-Learning Stationary Stochastic Process Prediction With Convolutional Neural Processes.pdf"
        authors="Foong, A. Y. K., Bruinsma W. P., Gordon. J., Dubois, Y., Requeima J., and Turner R. E."
        year="2020"
        title="Meta-Learning Stationary Stochastic Process Prediction with Convolutional Neural Processes"
        note="Advances in Neural Information Processing Systems (NeurIPS), 33th"
    %}
    {% include publication_entry.html
        file="publications/Bruinsma, 2020, Scalable Exact Inference in Multi-Output Gaussian Processes.pdf"
        authors="Bruinsma, W. P., Perim E., Tebbutt W., Hosking, J. S., Solin, A., and Turner, R. E."
        year="2020"
        title="Scalable Exact Inference in Multi-Output Gaussian Processes"
        note="International Conference on Machine Learning (ICML), 37th"
    %}
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
        note="Advances in Approximate Bayesian Inference (AABI), 2nd Symposium on"
    %}
    {% include publication_entry.html
        file="publications/Requeima, 2019, The Gaussian Process Autoregressive Regression Model (GPAR).pdf"
        authors="Requeima, J., Tebbutt W. C., Bruinsma, W. P., and Turner R. E."
        year="2019"
        title="The Gaussian Process Autoregressive Model (GPAR)"
        note="Artificial Intelligence and Statistics (AISTATS), 22nd International Conference on"
    %}
    {% include publication_entry.html
        file="arxiv/Bruinsma, 2018, Learning Causally-Generated Stationary Time Series.pdf"
        authors="Bruinsma, W. P. and Turner, R. E."
        year="2018"
        title="Learning Causally Generated Stationary Time Series"
        note="arXiv:1802.08167"
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
        url="https://www.youtube.com/watch?v=AIMOmfJInT8"
        authors="Bruinsma W. P., Requeima J., Foong, A. Y. K., Gordon. J., and Turner R. E."
        title="The Gaussian Neural Process (AABI 2020) <span class=\"tag\">video</span>"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, The Gaussian Neural Process (Handout).pdf"
        authors="Bruinsma W. P., Requeima J., Foong, A. Y. K., Gordon. J., and Turner R. E."
        title="The Gaussian Neural Process (AABI 2020)"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, On Sparse Variational Methods and the KL Divergence Between Stochastic Processes (Handout).pdf"
        authors="Bruinsma, W. P."
        title="On Sparse Variational Method and the KL Between Stochastic Processes"
    %}
    {% include publication_entry.html
        file="talks/Hron, Sequential Inference and Decision Making (Handout).pdf"
        authors="Hron J., and Bruinsma, W. P."
        title="Sequential Inference and Decision Making"
    %}
    {% include publication_entry.html
        url="https://www.youtube.com/watch?v=nq6X-w5xgLo"
        authors="Bruinsma, W. P., Gordon J., and Turner, R. E."
        title="NeuralProcesses.jl: Composing Neural Processes with Flux (JuliaCon 2020) <span class=\"tag\">video</span>"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, NeuralProcesses.jl.pdf"
        authors="Bruinsma, W. P., Gordon J., and Turner, R. E."
        title="NeuralProcesses.jl: Composing Neural Processes with Flux (JuliaCon 2020)"
    %}
    {% include publication_entry.html
        url="https://www.youtube.com/watch?v=OJmkz2LAM4Q"
        authors="Bruinsma, W. P., Perim E., Tebbutt W., Hosking, J. S., Solin, A., and Turner, R. E."
        title="Scalable Exact Inference in Multi-Output Gaussian Processes (ICML 2020) <span class=\"tag\">video</span>"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, Scalable Exact Inference in Multi-Output Gaussian Processes (Handout).pdf"
        authors="Bruinsma, W. P., Perim E., Tebbutt W., Hosking, J. S., Solin, A., and Turner, R. E."
        title="Scalable Exact Inference in Multi-Output Gaussian Processes (ICML 2020)"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, Compositional Model Design, High-Dimensional Multi-Output Regression (Handout).pdf"
        authors="Bruinsma, W. P."
        title="Compositional Model Design: High-Dimensional Multi-Output Regression"
    %}
    {% include publication_entry.html
        file="talks/Bruinsma, Points and Circles.pdf"
        authors="Bruinsma, W. P."
        title="Points and Circles"
    %}
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