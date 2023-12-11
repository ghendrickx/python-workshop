"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename: str) -> np.ndarray:
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    :type filename: str

    :return: Inflammation data
    :rtype: numpy.ndarray
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data: np.ndarray) -> np.ndarray:
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: Inflammation data
    :type data: numpy.ndarray

    :return: Daily mean of inflammation data
    :rtype: numpy.ndarray
    """
    return np.mean(data, axis=0)


def daily_max(data: np.ndarray) -> np.ndarray:
    """Calculate the daily max of a 2D inflammation data array.

    :param data: Inflammation data
    :type data: numpy.ndarray

    :return: Daily maximum of inflammation data
    :rtype: numpy.ndarray
    """
    return np.max(data, axis=0)


def daily_min(data: np.ndarray) -> np.ndarray:
    """Calculate the daily min of a 2D inflammation data array.

    :param data: Inflammation data
    :type data: numpy.ndarray

    :return: Daily minimum of inflammation data
    :rtype: numpy.ndarray
    """
    return np.min(data, axis=0)
