# An Improved Three-Phase Lag Bio-Heat Transfer Model for Human Tissue

Matthew Woods (m3woods@ucsd.edu)  
Alon Pavlov (alpavlov@ucsd.edu)

> **NOTE (GitHub Math):** GitHub renders LaTeX only with `$...$` (inline) and `$$...$$` (block).  
> Do **NOT** use `\[` `\]`. Keep **blank lines** before/after each `$$...$$` block.

---

## Abstract

Cryosurgery and heat-based ablation rely on precise thermal control to induce localized tissue necrosis while minimizing damage to surrounding tissue. Classical bio-heat models based on Fourier conduction often fail to capture transient behavior in heterogeneous tissue. This project implements and extends the three-phase lag (TPL) bio-heat transfer model by adding (i) evaporative cooling due to sweat and (ii) a fourth-kind boundary condition to better model conduction across two materials with different thermal conductivities. :contentReference[oaicite:0]{index=0}

---

## Governing Equations

### 1) Fourier Heat Conduction (Classical)

$$
\mathbf{q}(\mathbf{r},t) = -k \nabla T(\mathbf{r},t)
$$

- $\mathbf{q}$: heat flux vector  
- $k$: thermal conductivity  
- $T$: temperature field :contentReference[oaicite:1]{index=1}

---

### 2) Dual-Phase Lag (DPL) Model

$$
\mathbf{q}(\mathbf{r}, t+\tau_q) = -k \nabla T(\mathbf{r}, t+\tau_T)
$$

- $\tau_q$: heat-flux relaxation time  
- $\tau_T$: temperature-gradient relaxation time :contentReference[oaicite:2]{index=2}

---

### 3) Three-Phase Lag (TPL) Bio-Heat Model

Kumar & Kaur’s three-phase lag formulation (as presented in this report) is:

$$
\left(1+\tau_q \frac{\partial}{\partial t}\right)
\left(
\rho c \frac{\partial^2 T}{\partial t^2}
-\dot{Q}_b
-\dot{Q}_m
\right)
=
\left[
k^{*} + (k+k^{*}\tau_v)\frac{\partial}{\partial t}
+ k\tau_T \frac{\partial^2}{\partial t^2}
\right]
\left(
\frac{\partial^2 T}{\partial x^2}+\frac{\partial^2 T}{\partial y^2}
\right)
$$

- $\rho$: tissue density  
- $c$: tissue specific heat  
- $\dot{Q}_b$: blood perfusion heat source  
- $\dot{Q}_m$: metabolic heat source  
- $\tau_v$: thermal displacement relaxation time  
- $k^{*}$: modified conductivity term :contentReference[oaicite:3]{index=3}

---

## Initial and Symmetry Conditions

$$
T(x,y,0)=T_w
$$

$$
\frac{\partial T(x,y,0)}{\partial t}=0
$$

$$
\frac{\partial^2 T(x,y,0)}{\partial t^2}=0
$$

Symmetry (zero-gradient) conditions:

$$
-k\frac{\partial T(x,L,t)}{\partial x}=0,
\qquad
-k\frac{\partial T(L,y,t)}{\partial y}=0
$$
