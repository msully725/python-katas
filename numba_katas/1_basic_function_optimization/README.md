# Code Kata 1: Introduction to Numba with Basic Function Optimization

## Objective
Learn the basics of the Numba library by optimizing a simple Python function. This kata will introduce you to the `@jit` decorator, which is the cornerstone of using Numba for just-in-time compilation.

## Requirements
- Python installed
- Numba library installed (`pip install numba`)
- pytest installed for testing (`pip install pytest`)

## Step-by-Step Guide

### 1. Setup the Environment
Ensure you have a virtual environment set up and Numba installed. You can create a virtual environment and install Numba as follows:

```bash
python -m venv venv
source numba-kata-env/bin/activate  # On Windows use `numba-kata-env\Scripts\activate`
pip install numba pytest
```

### 2. Create the Function to Optimize

Create a Python function that computes the sum of squares of the first n natural numbers. This function will be optimized later using Numba.

### 3. Write the Test First (TDD Approach)

Create a test file test_sum_of_squares.py and write a test for the function.

```
# test_sum_of_squares.py

from sum_of_squares import sum_of_squares

def test_sum_of_squares():
    assert sum_of_squares(1) == 1
    assert sum_of_squares(2) == 5
    assert sum_of_squares(3) == 14
    assert sum_of_squares(10) == 385
 ```   

### 4. Implement the Initial Function

Create a file sum_of_squares.py and implement your function. Ensure it passes the tests you wrote.

### 5. Run the Tests

Run your tests to ensure your function works correctly.
```
pytest test_sum_of_squares.py
```

### 6. Optimize with Numba

Modify the function to use Numba’s @jit decorator. Research how to use the @jit decorator to optimize your function.

### 7. Re-run the Tests

Run your tests again to ensure your function still works correctly after optimization.

```
pytest test_sum_of_squares.py
```

### 8. Measure Performance

Write a script to compare the performance of the Numba-optimized function against the non-optimized version. Measure the time taken by each version for a large value of n.

### 9. Run the Benchmark

Execute the benchmark script to observe the performance improvement.

```
python benchmark.py
```