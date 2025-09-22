import numpy as np
import matplotlib.pyplot as plt


def numerical_range(A):
    min_x = []
    min_y = []
    max_x = []
    max_y = []
    for theta in np.linspace(0, 2 * np.pi, 100):
        A_j = A * np.exp(1j * theta)
        H_p = 1 / 2 * (A_j + A_j.conj().T)
        eigs, vecs = np.linalg.eigh(H_p)
        idx = eigs.argsort()[::-1]
        eigs = eigs[idx]
        vecs = vecs[:, idx]
        mino = vecs[:, 0].conj().T @ A @ vecs[:, 0] / (np.linalg.norm(vecs[:, 0]) ** 2)
        maxo = (
            vecs[:, -1].conj().T @ A @ vecs[:, -1] / (np.linalg.norm(vecs[:, -1]) ** 2)
        )
        min_x.append(np.real(mino))
        min_y.append(np.imag(mino))
        max_x.append(np.real(maxo))
        max_y.append(np.imag(maxo))

    plt.plot(max_x, max_y, label="maxes")
    # plt.plot(min_x, min_y, label="mins")


A = np.array([[1j, 1, 0], [0, 1j, 0], [0, 0, 1]])
A = np.array([[1j, 1, 0, 0], [0, 1j, 0, 0], [0, 0, 1 + 1j, 0], [0, 0, 0, -1]])
numerical_range(A)
plt.show()
# for i in range(2, 10):
#     A = np.zeros((i, i))
#     np.fill_diagonal(A[0:, 1:], 1)
#     numerical_range(A)
# plt.show()
