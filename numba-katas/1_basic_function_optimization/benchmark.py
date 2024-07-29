import timeit
from sum_of_squares import sum_of_squares, sum_of_squares_nojit

sample_n = 100000 
nojit_benchmark = timeit.timeit(lambda: sum_of_squares_nojit(sample_n), number=100)
print("Without JIT:", nojit_benchmark)

jit_benchmark = timeit.timeit(lambda: sum_of_squares(sample_n), number=100)
print("With JIT:", jit_benchmark)