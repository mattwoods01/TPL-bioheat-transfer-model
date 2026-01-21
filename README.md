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

Kumar &
