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


def daily_above_threshold(data: np.ndarray, patient_idx: int, threshold: int) -> float:
    """Determine whether or not each daily inflammation value exceeds a given threshold for a given
    patient.

    :param data: Inflammation data
    :param patient_idx: Patient index
    :param threshold: Inflammation threshold

    :type data: numpy.ndarray
    :type patient_idx: int
    :type threshold: int

    :return: Boolean list of days exceeding the threshold
    :rtype: list
    """
    # return np.sum(data[patient_idx] > threshold)
    return sum(map((lambda x: int(x > threshold)), data[patient_idx]))


def normalise_patient(data: np.ndarray) -> np.ndarray:
    """Normalise patient data from a 2D inflammation data array. Normalisation is per patient.

    :param data: Inflammation data
    :type data: numpy.ndarray

    :return: Normalised inflammation data
    :rtype: numpy.ndarray

    :raises TypeError: if `data` is not a `numpy.ndarray`
    :raises ValueError: if `data` is not two-dimensional
    :raises ValueError: if any values in `data` are negative
    """
    if not isinstance(data, np.ndarray):
        msg = f'`data`-argument must be a `numpy.ndarray`; {type(data)} given'
        raise TypeError(msg)

    if not len(data.shape) == 2:
        msg = f'`data`-argument should have two dimensions; {len(data.shape)} given'
        raise ValueError(msg)

    if np.any(data < 0):
        msg = 'Inflammation values should not be negative'
        raise ValueError(msg)

    data_max = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / data_max[:, np.newaxis]
    normalised[np.isnan(normalised) | (normalised < 0)] = 0
    return normalised
