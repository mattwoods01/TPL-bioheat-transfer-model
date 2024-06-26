import numpy as np
import matplotlib.pyplot as plt

# Constants and parameters
rho = 1000  # Tissue density (kg/m^3)
c = 4000  # Specific heat of tissue (J/kg°C)
k_list = [0.3, 0.625, 1, 1.5]  # Thermal conductivity of tissue (W/m°C)
k_star = 0.1 # Additional thermal conductivity term (W/m°C/s)
h = 4.5  # Heat transfer coefficient for Robin boundary condition (W/m^2°C) - Typical for large blood vessels
wb = 0.0098  # Blood perfusion rate coefficient (1/s) - Typical for skin tissue
rho_b = 1056  # Density of blood (kg/m^3)
cb = 4000  # Specific heat of blood (J/kg°C)
Qm0 = 50.65  # Metabolic heat generation (W/m^3)
Tb = 37  # Temperature of arterial blood (°C)
T0 = 37  # Initial temperature of the body (°C)
Tl = 37  # Temperature of Tissue (°C)
Tw = 100 # Fixed temperature at left and bottom boundary
Tw0 = 37
Lx = 0.05  # Length of the skin tissue in x direction (m)
Ly = 0.05  # Length of the skin tissue in y direction (m)
dx = 0.01  # Space step in x direction (m)
dy = 0.01  # Space step in y direction (m)
dt = 0.1  # Time step (s)
wall_temp_duration = 50 # Number of Wall Temperature 'ON' time steps
remove_wall_after = False # Remove Wall if True, disables fourth boundry condition on boundry border
fourth_boundary_on = True
time_steps = 100  # Number of time steps
tau_q = 600  # Relaxation time due to heat flux (s)
tau_T = 300  # Relaxation time due to temperature gradient (s)
tau_v = 100  # Relaxation time due to thermal displacement (s)
ambient_temp = 37 # Ambient temperature of space without initialized wall temp (°C)

# Constants for the second material (assuming for the boundary condition of fourth kind)
ku = 0.625   # Thermal conductivity of left material (W/m°C)

DOI_1 = 'https://doi.org/10.1016/j.ijthermalsci.2022.108002'

if wall_temp_duration == time_steps:
    remove_wall_after = False

# Boundry between wall and tissue
def wall_boundary(T_array, wall_temp):
    T_array[-1, :] = wall_temp  # x = 0 (bottom boundary)
    T_array[:, 0] = wall_temp  # y = 0 (left boundary)

# Symmetrical boundary conditions from eq. 16
def symmetric_boundary(T_array):
    T_array[0, :] = T_array[1, :]  # x = Lx
    T_array[-1, :] = T_array[-2, :]  # x = 0
    T_array[:, 0] = T_array[:, 1]  # y = 0
    T_array[:, -1] = T_array[:, -2]  # y = Ly

# Convective boundary condition to introduce a constant heat coefficient
def convective_boundary(T_array):
    T_array[0, :] = (h * dx * Tl + k * T_array[1, :]) / (h * dx + k)  # x = Lx
    T_array[:, -1] = (h * dx * Tl + k * T_array[:, -2]) / (h * dx + k)  # y = Ly

# Fourth boundary using constant temperature and heat flux for two thermal conductivity terms from secondary paper to model conduction.
def fourth_boundary(T_array):
    if fourth_boundary_on is True:
        T_array[-1, :] = T_array[-2, :] - (k / ku) * (T_array[-2, :] - T_array[-3, :])  # x = 0
        T_array[:, 0] = T_array[:, 1] - (ku / k) * (T_array[:, 1] - T_array[:, 2])  # y = 0

# Third boundary using constant heat coefficient 
def third_boundary(T_array):
    T_array[-1, :] = (h * dx * Tl + k * T_array[-2, :]) / (h * dx + k)  # x = 0
    T_array[:, 0] = (h * dx * Tl + k * T_array[:, 1]) / (h * dx + k)  # y = 0

# Discretization
x = np.arange(0, Lx + dx, dx)
y = np.arange(0, Ly + dy, dy)
nx = len(x)
ny = len(y)

# Initialize time derivatives
dTdt_initial = np.zeros((nx, ny))  # Initial first time derivative of temperature
d2Tdt2_initial = np.zeros((nx, ny))  # Initial second time derivative of temperature

# Initialize temperature fields
T_initial = np.ones((nx, ny)) * T0  # Initialize entire temperature field to T0
T_new_initial = np.ones((nx, ny)) * T0  # Initialize entire temperature field to T0

# Plotting the results
time = np.arange(0, time_steps * dt, dt)
plt.figure(figsize=(10, 6))

for k in k_list:
    # Copy time derivatives
    dTdt = dTdt_initial.copy()
    d2Tdt2 = d2Tdt2_initial.copy()

    # Copy temperature fields
    T = T_initial.copy()
    T_new = T_new_initial.copy()
    
    # Check if wall is initialized
    if wall_temp_duration > 0:
        wall_boundary(T, Tw)
        wall_boundary(T_new, Tw)

    # Else use ambient temperature of air
    elif wall_temp_duration == 0 and remove_wall_after is False:
        wall_boundary(T, Tw0)
        wall_boundary(T_new, Tw0)

    elif wall_temp_duration == 0 and remove_wall_after is True:
        wall_boundary(T, ambient_temp)
        wall_boundary(T_new, ambient_temp)

    # Store temperature profile at each time step
    temperature_profile = []

    # Time integration
    for t in range(time_steps):  
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                # From eq. 5
                Qm = Qm0 * (1 + (Tl - T0) / 10)

                #From eq. 6
                Qb = wb * rho_b * cb * (Tb - Tl)

                # Discretization using finite difference method
                d2Tdx2 = (T_new[i + 1, j] - 2 * T_new[i, j] + T_new[i - 1, j]) / dx ** 2
                d2Tdy2 = (T_new[i, j + 1] - 2 * T_new[i, j] + T_new[i, j - 1]) / dy ** 2

                # From eq. 4
                dTdt[i, j] = (k * (d2Tdx2 + d2Tdy2) + Qb + Qm) / (rho * c)

                # Derivative of eq. 4 with k* integrated
                d2Tdt2[i, j] = (k_star * (d2Tdx2 + d2Tdy2)) / (rho * c)

                # Substitute finite differences from discretization into eq. 7 and solve for T_n+1 
                T_new[i, j] = T[i, j] + dt * (dTdt[i, j] + tau_q * dTdt[i, j] - tau_T * d2Tdt2[i, j] + (k + k_star * tau_v) * dTdt[i, j])

        # Reapply fixed temperature boundary condition at each time step
        if t < wall_temp_duration:
            wall_boundary(T_new, Tw)

        # Symmetric boundary conditions (Neumann conditions with zero gradient)
        symmetric_boundary(T_new)

        # Reapply fixed temperature boundary condition at each time step
        if t < wall_temp_duration:
            wall_boundary(T_new, Tw)

        convective_boundary(T_new)
            
        # Robin boundary condition on all boundaries (convective)
        if t >= wall_temp_duration and remove_wall_after is True:
            print("both off")
            third_boundary(T_new)

        elif t >= wall_temp_duration and remove_wall_after is False:
            print("off")
            fourth_boundary(T_new)

        # Apply 4th boundry condition at boundry border between wall and tissue
        elif t < wall_temp_duration or remove_wall_after is False:
            print("on")
            fourth_boundary(T_new)

        elif t < wall_temp_duration or remove_wall_after is True:
            print("on")
            third_boundary(T_new)

        # Reapply fixed temperature boundary condition at each time step
        if t < wall_temp_duration:
            wall_boundary(T_new, Tw)

        # Update temperature
        T = T_new.copy()

        # Store temperature profile
        temperature_profile.append(T_new.copy())

    # Convert temperature profile to numpy array for easy slicing
    temperature_profile = np.array(temperature_profile)

    # Plot temperature at a specific point over time
    plt.plot(time, temperature_profile[:, nx // 2, ny // 2], label=f'k = {k} W/m°C')

plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Profile Over Time for Different k')
plt.legend()
plt.grid(True)
plt.savefig(f'temp_dur-{wall_temp_duration}_removewallafter-{remove_wall_after}_fourth-{fourth_boundary_on}.png')
# plt.show()

# Plot heatmaps for each k value
fig, axes = plt.subplots(1, len(k_list), figsize=(18, 6))

for idx, k in enumerate(k_list):
    # Copy time derivatives
    dTdt = dTdt_initial.copy()
    d2Tdt2 = d2Tdt2_initial.copy()

    # Copy temperature fields
    T = T_initial.copy()
    T_new = T_new_initial.copy()
    
    # Check if wall is initialized
    if wall_temp_duration > 0:
        wall_boundary(T, Tw)
        wall_boundary(T_new, Tw)

    # Else use ambient temperature of air
    elif wall_temp_duration == 0 and remove_wall_after is False:
        wall_boundary(T, Tw0)
        wall_boundary(T_new, Tw0)

    elif wall_temp_duration == 0 and remove_wall_after is True:
        wall_boundary(T, ambient_temp)
        wall_boundary(T_new, ambient_temp)

    # Store temperature profile at each time step
    temperature_profile = []

    # Time integration
    for t in range(time_steps):  
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                # From eq. 5
                Qm = Qm0 * (1 + (Tl - T0) / 10)

                #From eq. 6
                Qb = wb * rho_b * cb * (Tb - Tl)

                # Discretization using finite difference method
                d2Tdx2 = (T_new[i + 1, j] - 2 * T_new[i, j] + T_new[i - 1, j]) / dx ** 2
                d2Tdy2 = (T_new[i, j + 1] - 2 * T_new[i, j] + T_new[i, j - 1]) / dy ** 2

                # From eq. 4
                dTdt[i, j] = (k * (d2Tdx2 + d2Tdy2) + Qb + Qm) / (rho * c)

                # Derivative of eq. 4 with k* integrated
                d2Tdt2[i, j] = (k_star * (d2Tdx2 + d2Tdy2)) / (rho * c)

                # Substitute finite differences from discretization into eq. 7 and solve for T_n+1 
                T_new[i, j] = T[i, j] + dt * (dTdt[i, j] + tau_q * dTdt[i, j] - tau_T * d2Tdt2[i, j] + (k + k_star * tau_v) * dTdt[i, j])

        # Reapply fixed temperature boundary condition at each time step
        if t < wall_temp_duration:
            wall_boundary(T_new, Tw)

        # Symmetric boundary conditions (Neumann conditions with zero gradient)
        symmetric_boundary(T_new)

        # Reapply fixed temperature boundary condition at each time step
        if t < wall_temp_duration:
            wall_boundary(T_new, Tw)

        convective_boundary(T_new)
            
        # Robin boundary condition on all boundaries (convective)
        if t >= wall_temp_duration and remove_wall_after is True:
            third_boundary(T_new)

        elif t >= wall_temp_duration and remove_wall_after is False:
            fourth_boundary(T_new)

        # Apply 4th boundry condition at boundry border between wall and tissue
        elif t < wall_temp_duration or remove_wall_after is False:
            fourth_boundary(T_new)

        # Reapply fixed temperature boundary condition at each time step
        if t < wall_temp_duration:
            wall_boundary(T_new, Tw)

        # Update temperature
        T = T_new.copy()

    ax = axes[idx]  # Access the correct subplot
    T_rotated = np.rot90(T, -1)

    contour = ax.contourf(T_rotated, 100, cmap='hot')  # Transpose T for correct orientation
    fig.colorbar(contour, ax=ax, shrink=0.5)
    ax.set_aspect('equal', 'box') 
    ax.set_xlabel('Length in cm')
    ax.set_ylabel('Length in cm')
    ax.set_title(f'Temperature Distribution (k = {k}W/m°C)')

plt.tight_layout()
plt.savefig(f'temp_dur-{wall_temp_duration}_removewallafter-{remove_wall_after}_fourth-{fourth_boundary_on}_HM.png')
# plt.show()
