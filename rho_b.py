import numpy as np
import matplotlib.pyplot as plt

# Constants and parameters
rho = 1000  # Tissue density (kg/m^3)
c = 4000  # Specific heat of tissue (J/kg°C)
k = 0.625  # Thermal conductivity of tissue (W/m°C)
k_star = 0.01  # Additional thermal conductivity term (W/m°C/s)
h = 4.5  # Heat transfer coefficient for Robin boundary condition (W/m^2°C) - Typical for large blood vessels
wb = 0.0098  # Blood perfusion rate coefficient (1/s) - Typical for skin tissue
rho_b_list = [1005, 1056, 1080]  # Density of blood (kg/m^3)
cb = 4000  # Specific heat of blood (J/kg°C)
Qm0 = 50.65  # Metabolic heat generation (W/m^3)
Tb = 37  # Temperature of arterial blood (°C)
T0 = 37  # Initial temperature of the body (°C)
Tl = 37  # Temperature of Tissue (°C)
Tw = 39.3  # Fixed temperature at left and bottom boundary
Lx = 0.05  # Length of the skin tissue in x direction (m)
Ly = 0.05  # Length of the skin tissue in y direction (m)
dx = 0.01  # Space step in x direction (m)
dy = 0.01  # Space step in y direction (m)
dt = 0.1  # Time step (s)
time_steps = 1000  # Number of time steps
tau_q = 600  # List of relaxation times due to heat flux (s)
tau_T = 300  # Relaxation time due to temperature gradient (s)
tau_v = 100  # Relaxation time due to thermal displacement (s)

# Constants for the second material (assuming for the boundary condition of fourth kind)
ku = 0.5  # Thermal conductivity of left material (W/m°C)
kv = 0.7  # Thermal conductivity of right material (W/m°C)

# Discretization
x = np.arange(0, Lx + dx, dx)
y = np.arange(0, Ly + dy, dy)
nx = len(x)
ny = len(y)

dTdt_initial = np.zeros((nx, ny))  # Initial first time derivative of temperature
d2Tdt2_initial = np.zeros((nx, ny))  # Initial second time derivative of temperature

# Initialize temperature field
T_initial = np.ones((nx, ny)) * T0  # Initialize entire temperature field to T0
T_new_initial = np.ones((nx, ny)) * T0  # Initialize entire temperature field to T0

# Plotting the results
time = np.arange(0, time_steps * dt, dt)
plt.figure(figsize=(10, 6))

for rho_b in rho_b_list:
    # Initialize time derivatives
    dTdt = dTdt_initial.copy()
    d2Tdt2 = d2Tdt2_initial.copy()

    T = T_initial.copy()
    T_new = T_new_initial.copy()

    # Store temperature profile at each time step
    temperature_profile = []

    # Time integration
    # Initialize time derivatives
    dTdt = dTdt_initial.copy()
    d2Tdt2 = d2Tdt2_initial.copy()

    T = T_initial.copy()
    T_new = T_new_initial.copy()

    T[0, :] = Tw  # x = 0
    T[:, 0] = Tw  # y = 0

    # Store temperature profile at each time step
    temperature_profile = []

    # Time integration
    for t in range(time_steps):
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                Qb = wb * rho_b * cb * (Tb - Tl)
                Qm = Qm0 * (1 + (Tl - T0) / 10)

                d2Tdx2 = (T[i + 1, j] - 2 * T[i, j] + T[i - 1, j]) / dx ** 2
                d2Tdy2 = (T[i, j + 1] - 2 * T[i, j] + T[i, j - 1]) / dy ** 2

                dTdt[i, j] = (k * (d2Tdx2 + d2Tdy2) + Qb + Qm) / (rho * c)
                d2Tdt2[i, j] = (k_star * (d2Tdx2 + d2Tdy2)) / (rho * c)

                T_new[i, j] = T[i, j] + dt * (dTdt[i, j] + tau_q * dTdt[i, j] - tau_T * d2Tdt2[i, j] + (k + k_star * tau_v) * dTdt[i, j])

        # Symmetric boundary conditions (Neumann conditions with zero gradient)
        T_new[0, :] = T_new[1, :]  # x = 0
        T_new[-1, :] = T_new[-2, :]  # x = Lx
        T_new[:, 0] = T_new[:, 1]  # y = 0
        T_new[:, -1] = T_new[:, -2]  # y = Ly

        # Heat flux continuity: -ku * dT/dx at x = 0 for left material equals -kv * dT/dx at x = 0 for right material
        T_new[1, :] = T_new[1, :] + (ku / kv) * (T_new[2, :] - T_new[1, :])

        # Robin boundary condition on all boundaries
        T_new[:, 0] = (T[:, 1] + h * dy / k * Tl) / (1 + h * dy / k)  # y = 0
        T_new[:, -1] = (T[:, -2] + h * dy / k * Tl) / (1 + h * dy / k)  # y = Ly

        # Update temperature
        T = T_new.copy()

        # Store temperature profile
        temperature_profile.append(T_new.copy())

    # Convert temperature profile to numpy array for easy slicing
    temperature_profile = np.array(temperature_profile)

    # Plot temperature at a specific point over time
    plt.plot(time, temperature_profile[:, nx // 2, ny // 2], label=f'rho_b = {rho_b}kg/m^3')

plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Profile Over Time for Different rho_b')
plt.legend()
plt.grid(True)
plt.show()

# Plot heatmaps for each k value
fig, axes = plt.subplots(1, len(rho_b_list), figsize=(18, 6))

# Plotting the results
time = np.arange(0, time_steps * dt, dt)

for idx, rho_b in enumerate(rho_b_list):
    # Initialize time derivatives
    dTdt = dTdt_initial.copy()
    d2Tdt2 = d2Tdt2_initial.copy()

    T = T_initial.copy()
    T_new = T_new_initial.copy()

    T[0, :] = Tw  # x = 0
    T[:, 0] = Tw  # y = 0

    for t in range(time_steps):
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                Qb = wb * rho_b * cb * (Tb - Tl)
                Qm = Qm0 * (1 + (Tl - T0) / 10)

                d2Tdx2 = (T[i + 1, j] - 2 * T[i, j] + T[i - 1, j]) / dx ** 2
                d2Tdy2 = (T[i, j + 1] - 2 * T[i, j] + T[i, j - 1]) / dy ** 2

                dTdt[i, j] = (k * (d2Tdx2 + d2Tdy2) + Qb + Qm) / (rho * c)
                d2Tdt2[i, j] = (k_star * (d2Tdx2 + d2Tdy2)) / (rho * c)

                T_new[i, j] = T[i, j] + dt * (dTdt[i, j] + tau_q * dTdt[i, j] - tau_T * d2Tdt2[i, j] + (k + k_star * tau_v) * dTdt[i, j])

        # Symmetric boundary conditions (Neumann conditions with zero gradient)
        T_new[0, :] = T_new[1, :]  # x = 0
        T_new[-1, :] = T_new[-2, :]  # x = Lx
        T_new[:, 0] = T_new[:, 1]  # y = 0
        T_new[:, -1] = T_new[:, -2]  # y = Ly

        # Robin boundary condition on all boundaries
        T_new[:, 0] = (T[:, 1] + h * dy / k * Tl) / (1 + h * dy / k)  # y = 0
        T_new[:, -1] = (T[:, -2] + h * dy / k * Tl) / (1 + h * dy / k)  # y = Ly

        # Heat flux continuity: -ku * dT/dx at x = 0 for left material equals -kv * dT/dx at x = 0 for right material
        T_new[1, :] = T_new[1, :] + (ku / k) * (T_new[2, :] - T_new[1, :])

        # Update temperature
        T = T_new.copy()

    # Plot temperature distribution at the final time step
    X, Y = np.meshgrid(x, y)
    ax = axes[idx]
    contour = ax.contourf(X, Y, T.T, 20, cmap='hot')  # Transpose T for correct orientation
    fig.colorbar(contour, ax=ax)
    ax.set_xlabel('Length in cm')
    ax.set_ylabel('Length in cm')
    ax.set_title(f'Temperature Distribution (rho_b = {rho_b}kg/m^3)')

plt.tight_layout()
plt.show()
