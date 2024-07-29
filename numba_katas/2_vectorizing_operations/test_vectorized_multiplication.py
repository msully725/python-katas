import numpy as np
from vectorized_multiplication import vectorized_multiplication

def test_vectorized_multiplication():
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    result = vectorized_multiplication(a, b)
    expected = np.array([5, 12, 21, 32])
    np.testing.assert_array_equal(result, expected)