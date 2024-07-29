# Code Kata 2: Vectorizing Operations with Numba

## Objective

Learn to use Numba to vectorize operations and optimize performance for array-based computations. This kata will introduce you to Numba’s support for numpy arrays and how to leverage it for efficient numerical operations.

## Requirements

* Python installed
* Numba library installed (pip install numba)
* pytest installed for testing (pip install pytest)

## Step by Step Guide

### 1. Setup the Environment

Ensure you have a virtual environment set up and Numba installed. If you already have a virtual environment from Kata 1, you can use the same environment.

### 2. Write the Test First (TDD Approach)

Create a test file test_vectorized_multiplication.py and write tests for your function to ensure it works correctly. Here are some test cases to consider:

```python
# test_vectorized_multiplication.py

import numpy as np
from vectorized_multiplication import vectorized_multiplication

def test_vectorized_multiplication():
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    result = vectorized_multiplication(a, b)
    expected = np.array([5, 12, 21, 32])
    np.testing.assert_array_equal(result, expected)
```

### 3. Create a Vectorized Function

Write a function that computes the element-wise multiplication of two numpy arrays. This function will later be optimized using Numba.

### 4. Implement the Initial Function

Create the file vectorized_multiplication.py and implement your function. Ensure it passes the tests you wrote.

### 5. Run the Tests

Run your tests to ensure your function works 
correctly.
```
pytest test_vectorized_multiplication.py
```

### 6. Optimize with Numba

Modify the function to use Numba’s @jit decorator for vectorized operations. Research how to use Numba with numpy arrays.

### 7. Re-run the Tests

Run your tests again to ensure your function still works correctly after optimization.
```
pytest test_vectorized_multiplication.py
```

### 8. Measure Performance

Write a script to compare the performance of the Numba-optimized function against the non-optimized version. Measure the time taken by each version for large numpy arrays.

### 9. Run the Benchmark

Execute the benchmark script to observe the performance improvement.
```
python benchmark.py
```