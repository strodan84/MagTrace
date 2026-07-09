import numpy as np
import matplotlib.pyplot as plt


def plot_field_line(solution, ax=None, show=True):
    """
    Plot a traced magnetic field line in 3D.

    Parameters
    ----------
    solution : dict
        Dictionary returned by FieldTracer.trace()

    ax : matplotlib.axes._subplots.Axes3DSubplot, optional
        Existing 3D axis.

    show : bool
        Whether to display the figure.

    Returns
    -------
    fig, ax
    """

    x = solution["x"]
    y = solution["y"]
    z = solution["z"]

    if ax is None:
        fig = plt.figure(figsize=(7, 7))
        ax = fig.add_subplot(111, projection="3d")
    else:
        fig = ax.figure

    ax.plot(
        x,
        y,
        z,
        linewidth=2,
        label="Field Line"
    )

    ax.scatter(
        x[0],
        y[0],
        z[0],
        s=50,
        marker="o",
        label="Start"
    )

    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    ax.set_title("Magnetic Field Line")

    # ---------- Equal aspect ratio ----------
    max_range = np.array([
        x.max() - x.min(),
        y.max() - y.min(),
        z.max() - z.min()
    ]).max()

    x_mid = (x.max() + x.min()) / 2
    y_mid = (y.max() + y.min()) / 2
    z_mid = (z.max() + z.min()) / 2

    ax.set_xlim(x_mid - max_range/2, x_mid + max_range/2)
    ax.set_ylim(y_mid - max_range/2, y_mid + max_range/2)
    ax.set_zlim(z_mid - max_range/2, z_mid + max_range/2)

    ax.legend()

    if show:
        plt.show()

    return fig, ax