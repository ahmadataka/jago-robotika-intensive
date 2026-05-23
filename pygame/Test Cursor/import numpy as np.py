import numpy as np
import matplotlib.pyplot as plt

# System parameters
m = 1.0    # Mass (kg)
k = 20.0   # Spring constant (N/m)
c = 3.0    # Damping coefficient (N·s/m)

# PID controller parameters
Kp = 350.0   # Proportional gain
Ki = 300.0   # Integral gain
Kd = 50.0    # Derivative gain

# Simulation parameters
dt = 0.001   # Time step (s)
t_end = 5.0  # Simulation duration (s)
t = np.arange(0, t_end, dt)

# Desired position (setpoint)
x_target = 1.0

# State variables initialization
x = 0.0     # Position
v = 0.0     # Velocity
a = 0.0     # Acceleration

# For PID
integ_error = 0.0
prev_error = 0.0

# For storing simulation results
x_list = []
v_list = []
u_list = []

for i in range(len(t)):
    # Calculate error
    error = x_target - x
    integ_error += error * dt
    deriv_error = (error - prev_error) / dt

    # PID control force
    u = Kp*error + Ki*integ_error + Kd*deriv_error

    # Dynamics (Newton's 2nd Law): m*a = u - c*v - k*x
    a = (u - c * v - k * x) / m

    # Euler integration for v and x
    v += a * dt
    x += v * dt

    # Store for plotting
    x_list.append(x)
    v_list.append(v)
    u_list.append(u)

    prev_error = error

# Plotting results
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x_list, label='Position')
plt.axhline(x_target, color='r', linestyle='--', label='Target')
plt.xlabel('Time (s)')
plt.ylabel('Position (m)')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, v_list, label='Velocity', color='g')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()