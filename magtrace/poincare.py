import numpy as np
import matplotlib.pyplot as plt

def poincare_section(solution):
    """
    Compute intersections with the y=0 plane.

    Returns
    -------
    R, Z arrays
    """

    x = solution["x"]
    y = solution["y"]
    z = solution["z"]

    R_points = []
    Z_points = []

    for i in range(len(y)-1):

        if y[i] < 0 and y[i+1] >= 0:

            R = np.sqrt(x[i]**2 + y[i]**2)

            R_points.append(R)
            Z_points.append(z[i])

    return np.array(R_points), np.array(Z_points)

def plot_poincare(solution):

    R, Z = poincare_section(solution)

    plt.figure(figsize=(6,6))

    plt.scatter(
        R,
        Z,
        s=8
    )

    plt.xlabel("Major Radius R")
    plt.ylabel("Z")

    plt.title("Poincaré Section")

    plt.axis("equal")

    plt.show()