# An Improved Three-Phase Lag Model for Heat Transfer in Human Tissue

**Authors:** Matthew Woods (m3woods@ucsd.edu), Alon Pavlov (alpavlov@ucsd.edu)  
**Source:** Project report PDF :contentReference[oaicite:0]{index=0}

---

## Overview

This repository documents and implements an improved **three-phase lag (TPL)** bio-heat transfer model for epidermal skin tissue, motivated by applications in **cryosurgery** (extreme cooling) and **heat ablation** (extreme heating). The work extends classical Fourier conduction by introducing multiple relaxation times and evaluates how boundary conditions (including a **fourth-kind/mixed interface condition**) alter predicted temperature profiles and spatial gradients in tissue.

Key additions explored:
- **Evaporative cooling of sweat** integrated into the energy balance formulation.
- **Fourth-kind boundary condition** to model conduction across an interface between two materials with different thermal conductivities.

---

## Model Background

### Fourier’s Law (Classical)
\[
\vec{q}(\mathbf{r},t) = -k \nabla T(\mathbf{r},t)
\]
where \( \vec{q} \) is heat flux, \( k \) thermal conductivity, and \( T \) temperature :contentReference[oaicite:1]{index=1}.

### Dual-Phase Lag (DPL) (Tzou)
\[
\vec{q}(\mathbf{r}, t+\tau_q) = -k \nabla T(\mathbf{r},t)
\]
A lag is introduced between applied temperature gradient and resulting heat flux via relaxation time \( \tau_q \) :contentReference[oaicite:2]{index=2}.

### Three-Phase Lag (TPL) Bio-Heat Model (Kumar & Kaur)

The report combines the lagged conduction form with an energy balance including perfusion and metabolism to yield the TPL expression (as presented in the report):

\[
\left(1+\tau_q \frac{\partial}{\partial t}\right)
\left(
\rho c \frac{\partial^2 T}{\partial t^2} - \dot{Q}_b - \dot{Q}_m
\right)
=
\left(
k^* + (k + k^*\tau_v)\frac{\partial}{\partial t}
+ k\tau_T \frac{\partial^2}{\partial t^2}
\right)
\left(
\frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2}
\right)
\]
with tissue density \( \rho \), specific heat \( c \), perfusion heat term \( \dot{Q}_b \), metabolic term \( \dot{Q}_m \), and lag parameters \( \tau_q, \tau_T, \tau_v \) :contentReference[oaicite:3]{index=3}.

---

## Initial and Symmetry Conditions

Initial conditions:
\[
T(x,y,0)=T_w,\quad
\frac{\partial T(x,y,0)}{\partial t}=0,\quad
\frac{\partial^2 T(x,y,0)}{\partial t^2}=0
\]
:contentReference[oaicite:4]{index=4}.

Symmetry (zero gradient) conditions:
\[
-k\frac{\partial T(x,L,t)}{\partial x}=0,\quad
-k\frac{\partial T(L,y,t)}{\partial y}=0
\]
:contentReference[oaicite:5]{index=5}.

---

## Boundary Conditions

The report states a general boundary form:
\[
A_1\frac{\partial T(0,y,t)}{\partial x}+B_1 T(0,y,t)=f_1(y,t)
\]
\[
A_2\frac{\partial T(x,0,t)}{\partial y}+B_2 T(x,0,t)=f_2(x,t)
\]
:contentReference[oaicite:6]{index=6}.

### 1) Dirichlet (First Kind)
Constant boundary temperature:
\[
T = T_w
\]
Parameterization in report:
- \(A_1=0, B_1=1, f_1=T_w\)
- \(A_2=0, B_2=1, f_2=T_w\) :contentReference[oaicite:7]{index=7}.

### 2) Neumann (Second Kind)
Constant heat flux:
\[
-k\frac{\partial T}{\partial n}=q_w
\]
Parameterization in report:
- \(A_1=-k, B_1=0, f_1=q_w\)
- \(A_2=-k, B_2=0, f_2=q_w\) :contentReference[oaicite:8]{index=8}.

### 3) Robin (Third Kind)
Convective exchange:
\[
-k\frac{\partial T}{\partial n}=h(T-T_p)
\]
Parameterization in report:
- \(A_1=-k, B_1=h, f_1=hT_p\)
- \(A_2=-k, B_2=h, f_2=hT_p\) :contentReference[oaicite:9]{index=9}.

### 4) Fourth Kind (Mixed Interface Condition) — Added in This Project

Used to model an interface between two materials with different conductivities \(k_u\) and \(k_v\) and temperatures \(u\) and \(v\):

\[
u(0,t)=v(0,t),\quad t\in[0,t^*)
\]
\[
-k_u\frac{\partial u}{\partial x}\bigg|_{x=0}
=
-k_v\frac{\partial v}{\partial x}\bigg|_{x=0},\quad t\in[0,t^*)
\]
:contentReference[oaicite:10]{index=10}.

This was implemented via finite difference approximations at the tissue–wall interface (shared boundary).

---

## Improvement 1: Evaporative Cooling Term

Evaporative heat loss due to sweat is modeled as:
\[
\dot{Q}_{sweat}=\frac{S_i(P_{sk}-P_e)}{R_{va}}
\]
with
\[
R_{va}=\frac{2430\cdot 1000}{0.1353\sqrt{0.11+0.45V_w+V_e}}
\]
\[
P_{sk}=
\frac{(m_{rsw}R_{esk}R_{va})+(P_{sat}T_{sk}R_{va})+(P_eR_{esk})}{R_{esk}+R_{va}}
\]
:contentReference[oaicite:11]{index=11}.

The energy balance form becomes:
\[
(\dots -\dot{Q}_b-\dot{Q}_m+\dot{Q}_{sweat}) = \dots
\]
(as shown in Eq. (20) in the report) :contentReference[oaicite:12]{index=12}.

---

## Experimental Design (As Reported)

Three experiments were run for a 2D \(5\times 5\) cm tissue patch with heating applied for 5 s and total simulation time 10 s:

| Experiment | Shared Boundary Type | Wall Used | 4th BC Used | Heat On (s) | Total (s) |
|---|---:|---:|---:|---:|---:|
| A: Timed Convection | 3rd (Robin) | No | No | 5 | 10 |
| B: Timed Direct     | 1st (Dirichlet) | Yes | No | 5 | 10 |
| C: Timed Conduction | 4th (Mixed) | Yes | Yes | 5 | 10 |

:contentReference[oaicite:13]{index=13}.

Thermal conductivities tested:
\[
k \in \{0.3,\ 0.625,\ 1.0,\ 1.5\}\ \text{W/m°C}
\]
with wall conductivity \(k_u=0.625\ \text{W/m°C}\) :contentReference[oaicite:14]{index=14}.

---

## Reported Results (Summary)

- The Robin/shared convection case cools fastest.
- The 4th boundary condition shows a sharper temperature drop immediately after wall heating stops (visible near ~5.5 s) compared to Dirichlet, suggesting improved capture of post-heating conduction into the wall.
- Spatial distributions differ: Dirichlet produces more linear gradients; 4th-kind produces curvature near the shared boundary consistent with conduction into a second material.

:contentReference[oaicite:15]{index=15}.

Evaporative cooling was found to be negligible under the chosen small-area conditions because \( \dot{Q}_{sweat} \) was small relative to perfusion and metabolic heat terms :contentReference[oaicite:16]{index=16}.

---

## Parameters Used (From Report)

Selected parameters (see Table 2 in report for full list) :contentReference[oaicite:17]{index=17}:
- \( \rho = 1000\ \text{kg/m}^3 \)
- \( c = 4000\ \text{J/kg°
