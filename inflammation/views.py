"""Module containing code for plotting inflammation data."""

import numpy as np
from matplotlib import pyplot as plt

from inflammation.models import Patient


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


def display_patient_record(patient: Patient) -> None:
    print(patient.name)
    for obs in patient.observations:
        print(obs.day, obs.value)
