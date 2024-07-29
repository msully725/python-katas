from numba import jit

def sum_of_squares_nojit(n):
    result = 0
    for i in range(1, n + 1):
        result += i ** 2
    return result

@jit
def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i * i
    return sum