import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Define the matrix A(t)
def A(t):
    # Diagonal mondromy with these eigenvalues
    a = 1 / 10
    b = 10
    A = (
        1
        / (2 * np.pi)
        * np.array(
            [
                [
                    np.log(a) * np.cos(t) ** 2 + np.log(b) * np.sin(t) ** 2,
                    (np.log(a) - np.log(b)) * np.sin(t) * np.cos(t) - 2 * np.pi,
                ],
                [
                    (np.log(a) - np.log(b)) * np.sin(t) * np.cos(t) + 2 * np.pi,
                    np.log(a) * np.sin(t) ** 2 + np.log(b) * np.cos(t) ** 2,
                ],
            ]
        )
    )
    # nilpotent
    a = 1 / 2
    A = (1 / (np.pi * 2)) * np.array(
        [
            [(np.log(a) - 2 * np.sin(t) * np.cos(t)), 2 * (-np.pi + np.cos(t) ** 2)],
            [-2 * (-np.pi + np.sin(t) ** 2), np.log(a) + 2 * np.sin(t) * np.cos(t)],
        ]
    )

    return A


# RHS of the ODE: dx/dt = A(t)x
def f(t, x):
    return A(t) @ x


# Runge-Kutta 4 step
def rk4_step(t, x, dt):
    k1 = f(t, x)
    k2 = f(t + dt / 2, x + dt / 2 * k1)
    k3 = f(t + dt / 2, x + dt / 2 * k2)
    k4 = f(t + dt, x + dt * k3)
    return x + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


# Parameters
t0, tmax, dt = 0.0, 4.0, 0.01
times = np.arange(t0, tmax, dt)

# Initial conditions grid
grid_points = 20
x_vals = np.linspace(-2, 2, grid_points)
y_vals = np.linspace(-2, 2, grid_points)
initial_conditions = np.array([(x, y) for x in x_vals for y in y_vals])

# Simulate trajectories
trajectories = np.zeros((len(times), len(initial_conditions), 2))

for idx, x0 in enumerate(initial_conditions):
    x = x0
    for ti, t in enumerate(times):
        trajectories[ti, idx] = x
        x = rk4_step(t, x, dt)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect("equal")
ax.set_title("Trajectories of x' = A(t)x")

scat = ax.scatter([], [], s=10, c="blue")


def init():
    scat.set_offsets(np.empty((0, 2)))
    return (scat,)


def update(frame):
    scat.set_offsets(trajectories[frame])
    return (scat,)


ani = animation.FuncAnimation(
    fig, update, frames=len(times), init_func=init, blit=True, interval=30
)

plt.close(fig)
ani.save("trajectories.mp4", writer="ffmpeg", fps=30)
