# Improved Three-Phase Lag Bio-Heat Transfer Model for Human Tissue

## Abstract
This repository presents an academic investigation into improved bio-heat transfer modeling for human skin tissue under extreme thermal conditions. The work is motivated by clinical applications such as cryosurgery and heat-based tumor ablation, where accurate prediction of temperature distribution is critical for effective treatment and damage minimization. The project extends prior three-phase lag bio-heat models by incorporating enhanced boundary interactions and physiological effects to better capture real tissue behavior during transient heating and cooling events. :contentReference[oaicite:0]{index=0}

---

## Background
Thermal-based medical procedures rely on precise control of heat transfer within biological tissue. Traditional bio-heat models often assume simplified boundary conditions and homogeneous material behavior, which can lead to inaccuracies when tissue is exposed to rapid heating or cooling. In practice, tissue thermal response is influenced by blood perfusion, metabolic heat generation, environmental interaction, and contact with materials of differing thermal conductivity.

This project builds on established bio-heat modeling literature and focuses on improving realism by refining how boundary conditions and material interfaces are treated.

---

## Objectives
The primary objectives of this work are:

- To improve transient bio-heat transfer modeling accuracy in human skin tissue
- To evaluate how different boundary conditions affect temperature evolution
- To model heat conduction between tissue and adjacent materials with different thermal properties
- To assess the influence of evaporative cooling due to sweating on tissue temperature

---

## Methods Overview
A two-dimensional numerical simulation framework was used to model heat transfer in a small patch of human skin tissue. The model incorporates physiological heat sources such as metabolic heat production and blood perfusion.

The following methodological components were evaluated:

- Multiple boundary condition types, including fixed temperature, convective heat transfer, and material-aware conduction boundaries
- Time-dependent heating and cooling scenarios
- Finite-difference numerical discretization for transient analysis
- Comparative experiments across a range of tissue thermal conductivity values

Simulations were implemented using Python and MATLAB for numerical computation and visualization.

---

## Boundary Condition Analysis
Several boundary interaction cases were investigated:

- Direct heating with fixed surface temperature
- Convective heat loss to the environment
- Heat conduction across a shared boundary between skin tissue and a secondary material

A key contribution of this work is the inclusion of a mixed boundary condition that enforces continuity of both temperature and heat flux across a shared interface, enabling more realistic modeling of skin in contact with external objects or surgical tools.

---

## Evaporative Cooling Modeling
A simplified physiological model of sweating was incorporated to examine heat loss due to evaporation at the skin surface. The model evaluates how skin temperature, air resistance, and sweating rate influence evaporative heat loss.

Under the tested conditions and surface area, evaporative cooling was found to have a relatively small effect compared to metabolic heat production and blood perfusion. However, the framework allows for future expansion to larger surface areas and different environmental conditions.

---

## Results Summary
Key findings from the simulations include:

- Convective boundary conditions result in the fastest cooling rates
- Mixed (material-aware) boundary conditions produce more realistic post-heating temperature decay
- Lower thermal conductivity leads to steeper spatial temperature gradients
- Ignoring material-to-material conduction can overestimate tissue temperature
- Evaporative cooling contributes minimally at small spatial scales but may be relevant in broader applications

---

## Significance
Accurate bio-heat modeling is essential for predicting tissue damage in medical procedures involving extreme temperatures. The improvements presented in this project enhance predictive capability by accounting for realistic boundary interactions and material properties. These refinements can inform safer device design, improved treatment planning, and better interpretation of thermal injury risk.

---

## Repository Contents
- Python simulation scripts for transient bio-heat modeling
- MATLAB scripts for evaporative cooling analysis
- Generated plots and temperature distribution visualizations
- Full academic project report (PDF)

---

## Authors
Matthew Woods  
Alon Pavlov  

University of California, San Diego

---

## Citation
If you use or reference this work, please cite the project report included in this repository.
