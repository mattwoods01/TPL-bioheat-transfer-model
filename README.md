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

:contentReference[oaicite:4]{index=4}

---

## Boundary Conditions

A general boundary form (as stated in the report) is:

$$
A_1 \frac{\partial T(0,y,t)}{\partial x} + B_1 T(0,y,t) = f_1(y,t)
$$

$$
A_2 \frac{\partial T(x,0,t)}{\partial y} + B_2 T(x,0,t) = f_2(x,t)
$$

:contentReference[oaicite:5]{index=5}

### 1) First Kind (Dirichlet: Constant Temperature)

$$
A_1=0,\;B_1=1,\;f_1(y,t)=T_w,
\qquad
A_2=0,\;B_2=1,\;f_2(x,t)=T_w
$$

:contentReference[oaicite:6]{index=6}

### 2) Second Kind (Neumann: Constant Heat Flux)

$$
A_1=-k,\;B_1=0,\;f_1(y,t)=q_w,
\qquad
A_2=-k,\;B_2=0,\;f_2(x,t)=q_w
$$

:contentReference[oaicite:7]{index=7}

### 3) Third Kind (Robin: Convection)

$$
A_1=-k,\;B_1=h,\;f_1(y,t)=hT_p,
\qquad
A_2=-k,\;B_2=h,\;f_2(x,t)=hT_p
$$

:contentReference[oaicite:8]{index=8}

---

## Model Enhancement 1: Evaporative Cooling (Sweat)

Heat loss due to evaporation:

$$
\dot{Q}_{sweat}=\frac{S_i\left(P_{sk}-P_e\right)}{R_{va}}
$$

Air-layer vapor resistance (as written in the report):

$$
R_{va}=\frac{2430\cdot 1000}{0.1353\cdot 0.11 + 0.45V_w + V_e}
$$

Skin vapor pressure:

$$
P_{sk}=
\frac{\left(m_{rsw}R_{esk}R_{va}\right)+\left(P_{sat}T_{sk}R_{va}\right)+\left(P_eR_{esk}\right)}
{R_{esk}+R_{va}}
$$

TPL equation with sweat term:

$$
\left(1+\tau_q \frac{\partial}{\partial t}\right)
\left(
\rho c \frac{\partial^2 T}{\partial t^2}
-\dot{Q}_b
