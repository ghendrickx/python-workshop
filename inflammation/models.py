"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains
inflammation data for a single patient taken over a number of days
and each column represents a single day across all patients.
"""
import time

import numpy as np
import typing


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


class Observation:
    """Observation in an inflammation study."""

    def __init__(self, day: int, value: int) -> None:
        self.day = day
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Person:

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


class Patient(Person):
    """Patient in one of the inflammation studies."""

    def __init__(self, name: str, observations: typing.List[Observation] = None) -> None:
        super().__init__(name)
        if observations is None:
            self.observations = []
        else:
            assert all(isinstance(obs, Observation) for obs in observations)
            self.observations = observations

    def __str__(self) -> str:
        return self.name

    def add_observation(self, value: int, day: int = None) -> Observation:
        if day is None:
            try:
                day = self.observations[-1]['day'] + 1
            except IndexError:
                day = 0

        new_obs = Observation(day, value)

        self.observations.append(new_obs)

        return new_obs

    @property
    def last_observation(self) -> dict:
        return self.observations[-1]


class Doctor(Person):
    """Doctor involved in an inflammation study."""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.patients = dict()

    def add_patient(self, patient: Patient) -> None:
        if not isinstance(patient, Patient):
            msg = f'The `patient` must be of type `Patient`; {type(patient)} given'
            raise TypeError(msg)

        if patient.name in self.patients:
            print(f'{patient} already added to {self} ({self.patients})')
            return

        self.patients.update({patient.name: patient})


def attach_names(data, names) -> list:
    assert len(data) == len(names), \
        f'Length of `data` and `names` should match: {len(data)} =/= {len(names)}'

    out = [
        dict(name=n, data=d) for d, n in zip(data, names)
    ]

    return out
