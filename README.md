# Cyclepoint toolkit for standardized non-linear analysis of the menstrual cycle

---

## Overview

This repository outlines an innovative and highly practical data-driven method which treats the cycle in a standardized, non-linear fashion with multiple major advantages including: increased data resolution and statistical power, reduced bias from individual variance in cycle length, and capacity for comprehensive characterization of menstrual cycle effects, capturing the full extent of variance in outcomes of interest across the menstrual cycle. 

We demonstrate the utility of this method using hormonal, behavioral, and neuroimaging data. This repository functions as an open-source toolkit to facilitate use of this approach by researchers interested in the menstrual cycle. The toolkit provides ready-to-use code for calculation of the standardized cyclepoint, as well as for conducting physiological, behavioral, and neuroimaging analysis, including an annotated pipeline for adaptation of cyclepoint to fMRI data.

---

 ## Toolkit elements

- **Cyclepoint calculation** 

Includes code for calculating cyclepoint. Required information is: current day of cycle, total cycle length. We recommend only relying on verifiable cycle information (e.g., that collected using an app or a calendar).
This section of the toolkit includes both the general cyclepoint calculation, which standardizes all participant cycles to a scale ranging from 0 (first day of cycle/start of follicular phase) to 1 (last fay of cycle/end of the luteal phase) in the same fashion, as well as the adjustedCyclepoint, for researchers interested in further scaling cyclepoint under the assumption that the luteal phase is less variable than the follicular phase. AdjustedCyclepoint adjusts scaling based on total cycle length and provides a more conservative estimate of point in cycle.

- **Hormone application** 

Includes annotated code applying cyclepoint to analysis and visualization of hormone data. The cyclepoint approach to hormone analysis is in line with the natural, non-linear changes in hormone levels across the cycle, and provides a sensitive estimate of hormonal data. This code set also provides basic physiological validation of the cyclepoint approach.
Please note that we used standardized hormone measures in our models, and recommend the same to researchers interested in utilizing this approach.
This set of code is applied on a mix of publicly available datasets (references for all published work are included in folder).

- **Behavioral application** 

Includes annoted code applying cyclepoint to behavioral data, using a [previously published](https://www.nature.com/articles/s41598-023-48628-x) category learning study as an example. This code also includes bootstrap resampling for additional validation of the cyclepoint method. The linked manuscript includes model comparison with traditional cycle phase-based categorical approaches.

- **Neuroimaging application** 

Includes code applying cyclepoint to 1) structural and 2) functional neuroimaging data. Structural analyses are conducted on an open access deep phenotyping [dataset](https://doi.org/10.18112/openneuro.ds002674.v1.0.6). Functional analyses require Python. We provide step-by-step annotated code for applying cyclepoint to fMRI data in order to extract significant clusters of non-linear cycle-related activation at wholebrain level. We defined significant clusters by a voxel wise threshold of p = 0.001 and cluster-extent threshold of p = 0.05.

---

## Required software

Most code in the toolkit runs in **R**, but **Python** is required for initial processing of fMRI data. For fMRI applications, you will also need to run level one analyses of the data in the software of your preferece (we use FEAT).

---

## Relevant references

If you are using cyclepoint in your work, please cite these papers:

Placeholder for methods pub

Perović, M., Heffernan, E. M., Einstein, G., & Mack, M. L. (2023). Learning exceptions to category rules varies across the menstrual cycle. Scientific Reports, 13(1), 21999. https://doi.org/10.1038/s41598-023-48628-x
