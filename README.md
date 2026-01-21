# An Improved Three‑Phase Lag Bio‑Heat Transfer Model

This repository contains the implementation, experiments, and analysis for an **improved three‑phase lag (TPL) bio‑heat transfer model** applied to human skin tissue. The model extends classical and dual‑phase lag formulations to better simulate heat transfer during **cryosurgery** and **heat‑based ablation** procedures.

---

## Overview

Thermal therapies such as cryosurgery and heat ablation rely on precise control of temperature distributions in tissue. Classical Fourier‑based bio‑heat models often fail to capture transient and heterogeneous thermal behavior observed in real tissue.

This project builds upon the three‑phase lag bio‑heat model by:

* Incorporating **three relaxation times** (heat flux, temperature gradient, and thermal displacement)
* Supporting **multiple boundary condition types** (Dirichlet, Neumann, Robin)
* Introducing a **fourth (mixed) boundary condition** to model conduction between materials with different thermal conductivities
* Adding **evaporative cooling due to sweating** to the energy balance equation

The goal is to improve physical realism and predictive accuracy for biomedical thermal simulations.

---

## Key Features

* **Three‑Phase Lag Bio‑Heat Equation**

  * Accounts for delayed heat propagation in heterogeneous tissue
  * Extends Pennes’ bio‑heat equation and dual‑phase lag models

* **Boundary Condition Support**

  * **1st kind (Dirichlet):** constant temperature
  * **2nd kind (Neumann):** constant heat flux
  * **3rd kind (Robin):** convective heat transfer
  * **4th kind (Mixed):** continuous temperature *and* heat flux across materials

* **Evaporative Cooling Model**

  * Includes sweat evaporation above a physiological temperature threshold
  * Captures effects of air resistance, sweating rate, and skin temperature

* **Finite Difference Numerical Solver**

  * 2D spatial discretization of skin tissue
  * Time‑dependent temperature evolution

* **Python and MATLAB Implementations**

  * Python: temperature profiles and 2D heat maps
  * MATLAB: evaporative cooling analysis and comparative plots

---

## Model Description

### Governing Equation

The three‑phase lag bio‑heat equation integrates:

* Conduction
* Blood perfusion heat transfer
* Metabolic heat generation
* Optional evaporative heat loss

Three relaxation times are used:

* `τq` – heat flux relaxation
* `τT` – temperature gradient relaxation
* `τv` – thermal displacement relaxation

This formulation better captures transient thermal responses compared to classical Fourier models.

---

## Boundary Conditions

| Type            | Description                   | Application                       |
| --------------- | ----------------------------- | --------------------------------- |
| 1st (Dirichlet) | Constant temperature          | Direct heating / cryogenic probes |
| 2nd (Neumann)   | Constant heat flux            | Laser / RF ablation               |
| 3rd (Robin)     | Convective boundary           | Heat exchange with environment    |
| 4th (Mixed)     | Continuous temperature & flux | Conduction between materials      |

The **fourth boundary condition** is a major contribution of this work, allowing realistic simulation of tissue in contact with materials of differing thermal conductivity.

---

## Experiments

Three experiments were performed using a 5×5 cm skin tissue domain:

1. **Timed Convection**

   * Robin boundary condition
   * Simulates convective heat loss

2. **Timed Direct Heating**

   * Dirichlet boundary condition
   * Fixed wall temperature

3. **Timed Conduction**

   * Fourth boundary condition
   * Models conduction to a second material

Each experiment applies heating for 5 s followed by cooling, analyzing temperature profiles and spatial distributions.

---

## Results Summary

* Convection boundaries produce the fastest cooling

* Fourth‑boundary conduction shows:

  * Faster initial temperature decline
  * More realistic heat dissipation after heating stops
  * Radial temperature gradients near the shared boundary

* Thermal conductivity strongly influences peak temperature and cooling rate

* Evaporative cooling has **minimal impact** under the tested conditions but provides a more physiologically complete model

---

## Code Structure

### Python

* Solves the 2D three‑phase lag equation
* Generates:

  * Temperature vs. time plots
  * 2D heat maps for different thermal conductivities
* Uses NumPy and Matplotlib

### MATLAB

* Analyzes evaporative cooling effects
* Compares heat loss vs:

  * Skin temperature
  * Sweating rate
  * Air vapor resistance

---

## Requirements

### Python

* Python ≥ 3.8
* NumPy
* Matplotlib

### MATLAB

* MATLAB R2020+ recommended

---

## How to Run

### Python

1. Install dependencies
2. Run the simulation script
3. Generated plots will be saved to disk

### MATLAB

1. Open the provided `.m` files
2. Run individual sections to generate figures

---

## Applications

* Cryosurgery planning
* Thermal ablation modeling
* Burn and hyperthermia prediction
* Biomedical heat transfer research

---

## Future Work

* Multi‑layer tissue modeling (epidermis, dermis, fat)
* Larger surface area evaporation effects
* Patient‑specific parameterization
* GPU‑accelerated solvers

---

## Authors

* **Matthew Woods** – [m3woods@ucsd.edu](mailto:m3woods@ucsd.edu)
* **Alon Pavlov** – [alpavlov@ucsd.edu](mailto:alpavlov@ucsd.edu)

---

## References

Key references include work by Kumar & Kaur on three‑phase lag bio‑heat transfer, Pennes’ bio‑heat equation, and prior studies on evaporative cooling and conduction boundary conditions.

---

## License

This project is intended for academic and research use.
