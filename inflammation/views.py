"""Module containing code for plotting inflammation data."""

import numpy as np
from matplotlib import pyplot as plt


def visualize(data_dict: dict) -> None:
    """Display plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    :type data_dict: dict
    """
    # TODO(lesson-design) Extend to allow saving figure to file

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)

    fig.tight_layout()

    plt.show()


def on_screen(data_dict: dict) -> None:
    """Print basic statistical properties of the inflammation data to the screen.

    :param data_dict: Dictionary of name -> data to plot
    :type data_dict: dict
    """
    print('\t'.join(data_dict.keys()))
    for v in zip(*data_dict.values()):
        print('\t'.join(map(str, np.round(v, 4))))
