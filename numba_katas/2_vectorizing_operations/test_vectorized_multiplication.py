import numpy as np
import pytest
from vectorized_multiplication import vectorized_multiplication

@pytest.mark.parametrize("a, b, expected", [
    ([1, 2, 3, 4], [5, 6, 7, 8], [5, 12, 21, 32]),
])
def test_vectorized_multiplication(a, b, expected):
    numpy_a = np.array(a)
    numpy_b = np.array(b)
    result = vectorized_multiplication(numpy_a, numpy_b)
    numpy_expected = np.array(expected)
    np.testing.assert_array_equal(result, numpy_expected)