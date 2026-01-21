# Improved Three-Phase Lag Bioheat Transfer Model

This repository contains the mathematical modeling, numerical simulations, and analysis presented in the project **“An Improved Three Phase Lag Model for Heat Transfer in Human Tissue.”** The work extends classical and modern bioheat transfer models to better simulate thermal behavior in human skin tissue during **cryosurgery** and **heat ablation** procedures.

## Overview

Thermal therapies such as cryosurgery and heat ablation rely on precise control of heat transfer to destroy diseased tissue while minimizing damage to surrounding healthy tissue. Classical Fourier-based heat conduction models often fail to capture the delayed thermal response observed in biological tissue.

This project builds upon the **three-phase lag (TPL) bioheat transfer model**, incorporating:

* Relaxation effects in heat flux, temperature gradient, and thermal displacement
* Multiple boundary condition formulations relevant to clinical scenarios
* Additional physiological and physical mechanisms to improve realism

## Key Contributions

### 1. Three-Phase Lag Bioheat Model

* Extension of Fourier’s law using **three relaxation times**:

  * Heat flux lag (τq)
  * Temperature gradient lag (τT)
  * Thermal displacement lag (τv)
* Coupling of the modified conduction law with an **energy balance equation** including:

  * Blood perfusion heat
  * Metabolic heat generation

### 2. Boundary Condition Analysis

The model supports and compares multiple boundary condition types:

* **First kind (Dirichlet):** Constant surface temperature
* **Second kind (Neumann):** Constant heat flux
* **Third kind (Robin):** Convective heat transfer
* **Fourth kind (Mixed):** Continuous temperature *and* heat flux across a shared boundary

The fourth boundary condition enables accurate modeling of **conduction between two materials with different thermal conductivities**, such as skin in contact with a heated or cooled object.

### 3. Evaporative Cooling via Sweat

* Incorporation of a simplified **evaporative cooling term** based on sweat production
* Accounts for:

  * Skin temperature threshold for sweating
  * Water vapor resistance of air and skin
  * Regulatory sweating rate
* Results show evaporative cooling has minimal impact at small surface scales but is sensitive to environmental conditions

## Numerical Methods

* **Finite Difference Method (FDM)** for spatial and temporal discretization
* Transformation of governing equations into solvable matrix differential equations
* Simulations performed on a **5 cm × 5 cm skin tissue patch**
* Time-dependent heating and cooling experiments under varying boundary conditions

## Experiments

Three primary heating scenarios were evaluated:

| Experiment | Boundary Condition | Description                            |
| ---------- | ------------------ | -------------------------------------- |
| A          | Third (Robin)      | Timed convective heating               |
| B          | First (Dirichlet)  | Timed direct heating                   |
| C          | Fourth (Mixed)     | Timed conduction between two materials |

Thermal conductivity of tissue was varied to study its effect on temperature gradients and cooling dynamics.

## Results Summary

* **Fourth boundary condition** produced faster initial cooling after heat removal and more realistic heat dissipation
* Models without conduction to a secondary material **overestimate tissue temperature**
* Lower tissue thermal conductivity resulted in steeper temperature gradients
* Evaporative cooling effects were orders of magnitude smaller than metabolic and perfusion heat terms under tested conditions

## Code

### Python

* Used for temperature profile simulations and heatmap generation
* Implements:

  * Finite difference solvers
  * Boundary condition switching
  * Time-dependent wall heating

### MATLAB

* Used for parametric analysis of evaporative cooling effects
* Generates plots for:

  * Heat loss vs. skin temperature
  * Heat loss vs. sweating rate
  * Heat loss vs. vapor resistance

## Project Structure (Suggested)

```
├── python/
│   ├── three_phase_lag_model.py
│   └── plotting_utils.py
├── matlab/
│   ├── evaporative_cooling_analysis.m
│   └── temperature_profile_qsweat.m
├── figures/
│   ├── temperature_profiles/
│   └── heatmaps/
├── report/
│   └── Project_Report.pdf
└── README.md
```

## Applications

* Cryosurgery probe design
* Heat ablation planning
* Burn and hyperthermia modeling
* Bioheat transfer research
* Medical device thermal safety analysis

## Future Work

* Layered tissue modeling (epidermis, dermis, fat)
* Larger surface-area simulations for sweating effects
* Patient-specific parameterization
* Coupling with perfusion and vascular network models

## References

Key references include work by Kumar & Kaur on three-phase lag bioheat modeling, Pennes’ classical bioheat equation, and extensions involving mixed boundary conditions and evaporative cooling models.

---

**Authors:**
Matthew Woods
Alon Pavlov

UC San Diego – Bioengineering


model using this paper: https://www.sciencedirect.com/science/article/pii/S1290072922005300?via%3Dihub#b3
