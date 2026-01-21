# An Improved Three-Phase Lag Bio-Heat Transfer Model for Human Tissue

**Matthew Woods** (m3woods@ucsd.edu)  
**Alon Pavlov** (alpavlov@ucsd.edu)

---

## Abstract

Cryosurgery and heat-based ablation techniques rely on precise thermal control to induce localized tissue necrosis while minimizing damage to surrounding healthy tissue. Classical bio-heat models based on Fourier’s law often fail to capture transient thermal behavior in heterogeneous biological media.  

This project implements and extends the **three-phase lag (TPL) bio-heat transfer model**, originally proposed by Kumar and Kaur, by introducing:  
1. **Evaporative cooling due to sweat**, and  
2. **A fourth-kind (mixed) boundary condition** accounting for conductive heat transfer between materials with differing thermal conductivities.

The enhanced model improves prediction accuracy for transient thermal behavior during cryosurgical and heat-ablation procedures, particularly near material interfaces.

---

## Background

Thermal therapies such as **cryosurgery** and **heat ablation** offer minimally invasive alternatives to traditional surgical excision. Their effectiveness depends on accurate modeling of heat transport in tissue, which is influenced by:

- Blood perfusion  
- Metabolic heat generation  
- Tissue heterogeneity  
- Boundary interactions with surgical instruments  

Classical Fourier heat conduction assumes instantaneous propagation of thermal signals, which is insufficient for biological tissues exhibiting delayed thermal responses. Phase-lag models address this limitation.

---

## Governing Equations

### Fourier Heat Conduction (Classical)

\[
\vec{q}(\mathbf{r}, t) = -k \nabla T(\mathbf{r}, t)
\]

where  
- \( \vec{q} \) is heat flux  
- \( k \) is thermal conductivity  
- \( T \) is temperature  

---

### Dual-Phase Lag (DPL) Model

To incorporate finite thermal response times, Tzou introduced relaxation delays:

\[
\vec{q}(\mathbf{r}, t + \tau_q) = -k \nabla T(\mathbf{r}, t + \tau_T)
\]

where  
- \( \tau_q \): heat-flux relaxation time  
- \( \tau_T \): temperature-gradient relaxation time  

---

### Three-Phase Lag Bio-Heat Equation

By coupling the DPL formulation with the bio-heat energy balance equation, the **three-phase lag (TPL)** model is obtained:

\[
\left(1 + \tau_q \frac{\partial}{\partial t}\right)
\left(
\rho c \frac{\partial^2 T}{\partial t^2}
- \dot{Q}_b
- \dot{Q}_m
\right)
=
\left[
k^*
+ (k + k^* \tau_v)\frac{\partial}{\partial t}
+ k \tau_T \frac{\partial^2}{\partial t^2}
\right]
\nabla^2 T
\]

where  

| Symbol | Description |
|------|-------------|
| \( \rho \) | Tissue density |
| \( c \) | Specific heat capacity |
| \( \dot{Q}_b \) | Blood perfusion heat |
| \( \dot{Q}_m \) | Metabolic heat generation |
| \( \tau_v \) | Thermal displacement relaxation |
| \( k^* \) | Modified thermal conductivity |

---

## Initial Conditions

\[
T(x,y,0) = T_w
\]

\[
\frac{\partial T(x,y,0)}{\partial t} = 0
\]

\[
\frac{\partial^2 T(x,y,0)}{\partial t^2} = 0
\]

Symmetry conditions:

\[
\frac{\partial T(x,L,t)}{\partial x} = 0, \quad
\frac{\partial T(L,y,t)}{\partial y} = 0
\]

---

## Boundary Conditions

### First Kind (Dirichlet — Constant Temperature)

\[
T = T_w
\]

Used to model cryosurgical probes maintaining a fixed temperature.

---

### Second Kind (Neumann — Constant Heat Flux)

\[
-k \frac{\partial T}{\partial n} = q_w
\]

Models energy-controlled heat ablation sources (e.g., lasers).

---

### Third Kind (Robin — Convective Heat Transfer)

\[
-k \frac{\partial T}{\partial n} = h (T - T_p)
\]

Accounts for convection between tissue and surrounding environment.

---

### Fourth Kind (Mixed — Conductive Interface)

Introduced in this work to model **two materials with different thermal conductivities**:

\[
u(0,t) = v(0,t)
\]

\[
-k_u \frac{\partial u}{\partial x} = -k_v \frac{\partial v}{\partial x}
\]

This boundary condition enables realistic simulation of tissue–instrument conduction.

---

## Model Enhancements

### 1. Evaporative Cooling from Sweat

Heat loss due to sweat evaporation is modeled as:

\[
\dot{Q}_{sweat} =
\frac{S_i (P_{sk} - P_e)}{R_{va}}
\]

where  
- \( S_i \): skin surface area  
- \( P_{sk} \): skin vapor pressure  
- \( P_e \): environmental pressure  
- \( R_{va} \): vapor resistance of air layer  

The energy balance equation becomes:

\[
\left(1 + \tau_q \frac{\partial}{\partial t}\right)
\left(
\rho c \frac{\partial^2 T}{\partial t^2}
- \dot{Q}_b
- \dot{Q}_m
+ \dot{Q}_{sweat}
\right)
= \dots
\]

---

### 2. Improved Conductive Boundary Modeling

The fourth-kind boundary condition enables heat transfer across materials with unequal \( k \), improving prediction of cooling rates once thermal sources are removed.

---

## Numerical Methods

- Finite Difference Method (FDM)  
- Dimensionless transformation  
- Time-marching explicit scheme  
- Implemented in **Python** and **MATLAB**

---

## Results Summary

- Fourth-kind boundary condition produces **faster initial cooling** and more realistic heat dissipation.
- Lower tissue thermal conductivity yields steeper temperature gradients.
- Evaporative cooling has minimal impact under small surface-area assumptions.
- Conductive interfaces significantly affect transient temperature profiles.

---

## Conclusion

This work extends the three-phase lag bio-heat model by incorporating evaporative cooling and a fourth-kind boundary condition. While sweat evaporation contributes minimally under controlled conditions, conductive boundary modeling substantially improves realism. These enhancements improve predictive accuracy for thermal therapies such as cryosurgery and heat ablation.

---

## References

Key reference used throughout this implementation:  
Kumar & Kaur, *International Journal of Thermal Sciences*, 2023.  
:contentReference[oaicite:0]{index=0}

---

## Repository Notes

- Equations are LaTeX-compatible for GitHub rendering  
- Code implementations available in Python and MATLAB  
- Figures reproduce temperature profiles and spatial distributions  

---

