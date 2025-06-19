# Thesis Project: Introducing c-VEP to Gaze-Independent BCIs: A Hybrid Approach with the P300 ERP and Alpha-Band Power

This repository contains all the notebooks and Python files used in this thesis. It begins with a brief overview of the thesis, followed by a description of the repository’s structure. Finally, notes on software versions and other important details are provided.

## Project description

The use of code-modulated visual evoked potentials (c-VEPs) within a covert attention paradigm is researched to develop a gaze-independent brain-computer interface (BCI). This approach addresses a gap in the current literature, where most gaze-independent BCIs have focused primarily on steady-state visual evoked potentials (SSVEPs) and event-related potentials (ERPs).

Furthermore, due to the specifics of the experiment, two additional neural markers are included: P300 and alpha. Experiments are done for every individual neural marker, but also for the hybrid version.

For the individual pipelines, experiments are done using several optimization techniques, such as:
1. Block-Toeplitz Linear Discriminant Analysis (BT-LDA) versus Shrinkage LDA (sLDA) for classification of both alpha and P300.

2.  Power Spectral Density (PSD) versus Common Spatial Patterns (CSP) for alpha feature extraction.

3. Independent Component Analysis (ICA) to remove eye artifacts for all pipelines.

## Overview
c-VEP --> straightforward, only experiments with and without ICA. For the others notebooks are used.



## Versions
