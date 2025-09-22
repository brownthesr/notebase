import numpy as np
import matplotlib.pyplot as plt

# Define A
A = np.array([[3, 1, 0], [1, 4, 1], [0, 1, 2]])


# Function to get A-norm
def A_norm(x):
    return np.sqrt(x.T @ A @ x)


# First CG direction from origin (let's assume it's the steepest descent)
b = np.array([1, 1, 1])
x0 = np.zeros(3)
r0 = b - A @ x0
p0 = r0 / np.linalg.norm(r0)

# Scale to A-sphere
p0_A = p0 / A_norm(p0)


# Find a basis of the plane conjugate to p0 (i.e., d s.t. d^T A p0 = 0)
# Let's use Gram-Schmidt in A-metric
def A_orthonormalize(vectors):
    ortho = []
    for v in vectors:
        for u in ortho:
            v = v - (v.T @ A @ u) / (u.T @ A @ u) * u
        if np.linalg.norm(v) > 1e-8:
            ortho.append(v / np.sqrt(v.T @ A @ v))
    return ortho


# Generate two random vectors and orthonormalize against p0
v1 = np.array([1, -1, 0])
v2 = np.array([0, 1, -1])

# Make them conjugate to p0 and to each other
basis = A_orthonormalize([v1, v2, p0])
v1_A, v2_A = basis[0], basis[1]

# Generate points in the plane
angles = np.linspace(0, 2 * np.pi, 100)
circle = np.array([np.cos(angles), np.sin(angles), np.zeros_like(angles)])
plane_points = v1_A[:, None] * circle[0] + v2_A[:, None] * circle[1]

# Shift to the tip of p0_A
plane_points = plane_points + p0_A[:, None]

# Create the A-sphere (ellipsoid)
u = np.linspace(0, np.pi, 50)
v = np.linspace(0, 2 * np.pi, 50)
X = np.outer(np.sin(u), np.cos(v))
Y = np.outer(np.sin(u), np.sin(v))
Z = np.outer(np.cos(u), np.ones_like(v))

# Scale to A-sphere
X_A, Y_A, Z_A = np.zeros_like(X), np.zeros_like(Y), np.zeros_like(Z)
for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        p = np.array([X[i, j], Y[i, j], Z[i, j]])
        p = p / A_norm(p)
        X_A[i, j], Y_A[i, j], Z_A[i, j] = p

# Plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X_A, Y_A, Z_A, color="lightblue", alpha=0.3, linewidth=0)

# Plot p0
ax.quiver(0, 0, 0, p0_A[0], p0_A[1], p0_A[2], color="red", linewidth=3, label="$p_0$")

# Plot the conjugate plane
ax.plot(
    plane_points[0],
    plane_points[1],
    plane_points[2],
    color="purple",
    label="A-conjugate plane to $p_0$",
)

ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title(
    "Conjugate Gradient Intuition in 3D\nA-ellipsoid, $p_0$, and Conjugate Plane"
)
ax.legend()
plt.show()
