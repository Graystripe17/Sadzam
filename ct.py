#!/usr/bin/python3
import pdb
import cmath
import math
import numpy as np

def fft(x):
    N = len(x)
    X = []
    for k in range(N):
        W_k = [cmath.exp(-2j * math.pi * n * k / N) for n in range(N)]
        X.append(sum([a * b for a, b in zip(W_k, x)]))
    return X

def is_power_of_two(n):
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0

def cooley_tukey_recursive(a):
    x = a.copy()
    # Algorithm must be power of two size input
    # Padding by zero yields the same results
    while not is_power_of_two(len(x)):
        x.append(0)
    def helper(x):
        N = len(x)
        if N <= 2:
            x_odd = [x[0]]
            x_even = [x[1]]
        else:
            x_odd = helper(x[:N:2])
            x_even = helper(x[1:N:2])
        half = N // 2
        W = [cmath.exp(-2j * math.pi * k / N) for k in range(half)]
        weighted_even = [even * w for even, w in zip(x_even, W)]
        begin = [x + w for x, w in zip(x_odd, weighted_even)]
        end = [x - w for x, w in zip(x_odd, weighted_even)]
        return begin + end
    return helper(x)

a = [0, 1, 4, 3, 8, 3, 0, 0, 0] 
F = fft(a)
C = cooley_tukey_recursive(a)
E = list(np.fft.fft(a))
print("F", F)
print("C", C)
print("E", E)
print(len(F), len(C), len(E))
for i in range(len(a)):
    print(F[i], C[i], E[i])
    assert(math.isclose(abs(F[i]), abs(E[i]), abs_tol=1e-8))
