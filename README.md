# Improved Three-Phase Lag Bio-Heat Transfer Model for Human Tissue

This repository presents an enhanced **three-phase lag (TPL) bio-heat transfer model** for simulating thermal transport in human skin tissue during **cryosurgery** and **heat-based ablation therapies**. The model extends classical bio-heat formulations by incorporating multiple thermal relaxation times, physiological heat sources, evaporative cooling due to sweating, and an improved boundary formulation for conduction between dissimilar materials.

The work is based on and extends the three-phase lag model proposed by Kumar and Kaur (2023), with additional physiological and boundary-condition refinements.

---

## Abstract

Cryosurgical and heat-induced ablation techniques rely on precise thermal control to induce localized tissue necrosis while minimizing collateral damage. Classical Fourier-based heat transfer models fail to capture delayed thermal responses in heterogeneous biological tissues. This work implements a three-phase lag bio-heat transfer model incorporating relaxation times associated with heat flux, temperature gradient, and thermal displacement. Additional improvements include evaporative cooling due to sweat and a fourth-kind boundary condition enabling continuous temperature and heat flux across interfaces with differing thermal conductivities. Numerical simulations demonstrate improved prediction of transient temperature profiles and boundary-driven heat dissipation.

---

## Background

Thermal therapies such as cryosurgery and hyperthermia-based ablation offer minimally invasive alternatives to conventional surgery. However, accurate prediction of tissue temperature evolution remains challenging due to tissue heterogeneity, blood perfusion, and transient boundary effects. To address these limitations, non-Fourier heat conduction models introduce finite thermal response times that better represent biological heat transport.

---

## Governing Equations

### Classical Fourier Heat Conduction

\[
\mathbf{q}(\mathbf{r},t) = -k \nabla T(\mathbf{r},t)
\]

where  
- \( \mathbf{q} \) is the heat flux vector  
- \( k \) is thermal conductivity  
- \( T \) is temperature  

---

### Dual-Phase Lag (DPL) Model

\[
\mathbf{q}(\mathbf{r}, t + \tau_q) = -k \nabla T(\mathbf{r}, t + \tau_T)
\]

where  
- \( \tau_q \) is the heat flux relaxation time  
- \( \tau_T \) is the temperature gradient relaxation time  

---

### Bio-Heat Energy Balance Equation

\[
\rho c \frac{\partial T}{\partial t}
=
\nabla \cdot (k \nabla T)
+
\dot{Q}_b
+
\dot{Q}_m
\]

where  
- \( \rho \) is tissue density  
- \( c \) is specific heat  
- \( \dot{Q}_b \) is blood perfusion heat generation  
- \( \dot{Q}_m \) is metabolic heat generation  

---

### Three-Phase Lag Bio-Heat Model

\[
\left(1 + \tau_q \frac{\partial}{\partial t}\right)
\left[
\rho c \frac{\partial^2 T}{\partial t^2}
-
\dot{Q}_b
-
\dot{Q}_m
\right]
=
\left[
k^* + (k + k^* \tau_v)\frac{\partial}{\partial t}
+ k \tau_T \frac{\partial^2}{\partial t^2}
\right]
\nabla^2 T
\]

where  
- \( \tau_v \) is the thermal displacement relaxation time  
- \( k^* \) is a higher-order thermal conductivity coefficient  

---

## Evaporative Cooling Due to Sweating

Heat loss from sweat evaporation is modeled as:

\[
\dot{Q}_{sweat} =
\frac{S_i (P_{sk} - P_e)}{R_{va}}
\]

where  
- \( S_i \) is the skin surface area  
- \( P_{sk} \) is the water vapor pressure at the skin surface  
- \( P_e \) is the environmental vapor pressure  
- \( R_{va} \) is the water vapor resistance of the air layer  

Sweat evaporation is activated only when skin temperature exceeds a physiological threshold of approximately **37.38 °C**.

---

## Boundary Conditions

### First Kind (Dirichlet)

\[
T = T_w
\]

Represents constant-temperature probes used in cryosurgery.

---

### Second Kind (Neumann)

\[
-k \frac{\partial T}{\partial n} = q_w
\]

Models constant heat flux sources such as lasers or microwave applicators.

---

### Third Kind (Robin)

\[
-k \frac{\partial T}{\partial n} = h (T - T_p)
\]

Represents convective heat exchange with the surrounding environment.

---

### Fourth Kind (Mixed / Conductive Interface)

\[
T_u(0,t) = T_v(0,t)
\]

\[
-k_u \frac{\partial T_u}{\partial x}
=
-k_v \frac{\partial T_v}{\partial x}
\]

This boundary condition enforces continuity of both temperature and heat flux across a shared boundary between materials with different thermal conductivities.

---

## Numerical Methodology

- **Spatial domain:** 5 cm × 5 cm 2D skin tissue patch  
- **Discretization:** Finite difference method  
- **Time integration:** Explicit time stepping  
- **Initial conditions:**
\[
T(x,y,0) = T_w,\quad
\frac{\partial T}{\partial t}\bigg|_{t=0} = 0
\]

- **Symmetry:** Zero-flux Neumann boundaries on non-heated edges  

Simulations were implemented in **Python** for temperature evolution and heatmaps, with **MATLAB** used for evaporative cooling analysis.

---

## Experiments

Three heating scenarios were evaluated:

| Experiment | Boundary Condition | Conductive Wall |
|----------|-------------------|----------------|
| A | Robin (3rd) | No |
| B | Dirichlet (1st) | Yes |
| C | Mixed (4th) | Yes |

Thermal conductivity values tested:

\[
k = \{0.3,\;0.625,\;1.0,\;1.5\}\;\text{W/m·°C}
\]

Heating was applied for 5 s at 100 °C, followed by passive cooling.

---

## Results Summary

- Mixed (fourth-kind) boundary conditions produced faster post-heating cooling and more realistic surface temperature curvature.
- Dirichlet boundaries consistently overestimated tissue temperature.
- Lower thermal conductivity resulted in steeper thermal gradients.
- Evaporative cooling had minimal impact at small surface areas but becomes significant under higher vapor resistance or larger exposed regions.

---

## Conclusion

Incorporating a fourth-kind boundary condition and three-phase lag dynamics significantly improves bio-heat transfer modeling accuracy near tissue interfaces. The enhanced model better captures transient heat dissipation and interfacial conduction effects relevant to cryosurgery, hyperthermia therapy, and burn prediction.

---

## References

A full list of references is provided in the accompanying project report, including foundational works by Pennes (1948), Tzou (2014), and Kumar & Kaur (2023).

---

## Author

**Matthew Woods**  
M.S. Bioengineering, UC San Diego  
Email: m3woods@ucsd.edu
