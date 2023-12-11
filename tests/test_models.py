"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean, daily_max, daily_min


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
def test_daily_max(test, expected):
    npt.assert_array_equal(daily_min(test), expected)


def test_daily_min_string():
    with pytest.raises(TypeError):
        daily_min(np.array([['Hello', 'there'], ['General', 'Kenobi']]))
