from ct import fft, cooley_tukey_recursive, cooley_tukey_iterative
import numpy as np
import math
from matplotlib import pyplot

a = [0, 1, 4, 3, 8, 3, 0, 2, 0, 4, 1, 1, 6, 8, 3, 1, 14, 23, 55]
F = fft(a)
C = cooley_tukey_recursive(a)
I = cooley_tukey_iterative(a)
E = list(np.fft.fft(a))
print("F", F)
print("C", C)
print("E", E)
print(len(F), len(C), len(E))
for i in range(len(a)):
    print(F[i], C[i], E[i])
    assert(math.isclose(abs(F[i]), abs(E[i]), abs_tol=1e-8))

time = range(len(a))
pyplot.plot(F, label='F')
pyplot.plot(C, label='C')
pyplot.plot(E, label='E')
pyplot.plot(a, label='a')
pyplot.legend()
pyplot.show()
