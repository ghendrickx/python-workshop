"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_max, daily_min, normalise_patient


@pytest.mark.parametrize(
    'test, expected',
    [
        (np.array([[0, 0], [0, 0], [0, 0]]), [0, 0]),
        (np.array([[1, 2], [3, 4], [5, 6]]), [3, 4])
    ]
)
def test_daily_mean(test, expected):
    npt.assert_array_equal(daily_mean(test), expected)


@pytest.mark.parametrize(
    'test, expected',
    [
        (np.array([[0, 0], [0, 0], [0, 0]]), [0, 0]),
        (np.array([[1, 2], [3, 4], [5, 6]]), [5, 6])
    ]
)
def test_daily_max(test, expected):
    npt.assert_array_equal(daily_max(test), expected)


@pytest.mark.parametrize(
    'test, expected',
    [
        (np.array([[0, 0], [0, 0], [0, 0]]), [0, 0]),
        (np.array([[1, 2], [3, 4], [5, 6]]), [1, 2])
    ]
)
def test_daily_min(test, expected):
    npt.assert_array_equal(daily_min(test), expected)


def test_daily_min_string():
    with pytest.raises(TypeError):
        daily_min(np.array([['Hello', 'there'], ['General', 'Kenobi']]))


@pytest.mark.parametrize(
    'test, expected, raising',
    [
        (
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            None
        ),
        (
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            None
        ),
        (
            [[float('nan'), 1, 1], [1, 1, 1], [1, 1, 1]],
            [[0, 1, 1], [1, 1, 1], [1, 1, 1]],
            None
        ),
        (
            [[1, 2, 3], [4, 5, float('nan')], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.8, 1, 0], [0.78, 0.89, 1]],
            None
        ),
        (
            [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            ValueError
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None
        )
    ]
)
def test_patient_normalise(test, expected, raising):
    if raising is None:
        npt.assert_almost_equal(normalise_patient(np.array(test)), np.array(expected), decimal=2)
    else:
        with pytest.raises(raising):
            npt.assert_almost_equal(
                normalise_patient(np.array(test)), np.array(expected), decimal=2
            )

