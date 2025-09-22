import numpy as np
import matplotlib.pyplot as plt
from os import listdir


def single_image_svd(image_name):
    filename = "data/" + image_name

    print(listdir())
    pixels = plt.imread(filename)
    plt.subplot(221)
    plt.imshow(pixels)
    plt.title("Before")

    for i, k in enumerate([5, 10, 15]):
        U, s, VT = np.linalg.svd(pixels)

        new_pix = U[:, :k] @ np.diag(s[:k]) @ VT[:k, :]
        plt.subplot(2, 2, i + 2)
        plt.title(f"rank {k} approximation")
        plt.imshow(new_pix)
        plt.tight_layout()
    plt.show()


def read_image(image_name):
    filename = "data/" + image_name
    pixels = plt.imread(filename)
    return pixels


def pca_thing(index):
    images = listdir("data/")
    li = []
    suffixes = []
    for image_n in images:
        li.append(read_image(image_n).flatten())
        suffixes.append(image_n.split(".")[-1])
    A = np.stack(li, axis=1)
    unique_suffixes = list(set(suffixes))
    suffix_to_num = {suf: i for i, suf in enumerate(unique_suffixes)}
    colors = [suffix_to_num[suf] for suf in suffixes]
    new_image = A[:, index].reshape((243, 320))
    plt.title("2d")
    A_c = A - A.mean(axis=1, keepdims=True)
    U, s, VT = np.linalg.svd(A, full_matrices=False)
    reduced_2d = U[:, :2].T @ A_c
    reduced_3d = U[:, :3].T @ A_c

    sc = plt.scatter(reduced_2d[0, :], reduced_2d[1, :], c=colors)

    cbar = plt.colorbar(sc, ticks=range(len(unique_suffixes)))
    cbar.ax.set_yticklabels(unique_suffixes)
    cbar.set_label("File Suffix")
    plt.show()
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection="3d")
    sc = ax.scatter(reduced_3d[0, :], reduced_3d[1, :], reduced_3d[2, :], c=colors)

    cbar = plt.colorbar(sc, ticks=range(len(unique_suffixes)))
    cbar.ax.set_yticklabels(unique_suffixes)
    cbar.set_label("File Suffix")
    plt.show()


def all_images(index):
    images = listdir("data/")
    li = []
    for image_n in images:
        li.append(read_image(image_n).flatten())
    A = np.stack(li, axis=1)
    new_image = A[:, index].reshape((243, 320))
    plt.subplot(2, 2, 1)
    plt.title("before")
    plt.imshow(new_image)
    U, s, VT = np.linalg.svd(A, full_matrices=False)
    print(s.shape)
    for i, k in enumerate([15, 60, 150]):
        A_r = U[:, :k] @ np.diag(s[:k]) @ VT[:k, :]
        new_image = A_r[:, index].reshape((243, 320))
        plt.subplot(2, 2, i + 2)
        plt.title(f"rank {k} approximation")
        plt.imshow(new_image)
    plt.tight_layout()
    plt.show()


all_images(2)
