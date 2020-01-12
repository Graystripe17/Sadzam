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

def cooley_tukey_recursive(x):
    N = len(x)
    # Algorithm must be power of two size input
    # Padding by zero yields the same results
    # while not is_power_of_two(N):
    #    x.append(0)
    if N <= 2:
        x_odd = [x[0]]
        x_even = [x[1]]
    else:
        x_odd = cooley_tukey_recursive(x[:N:2])
        x_even = cooley_tukey_recursive(x[1:N:2])
    half = N // 2
    W = [cmath.exp(-2j * math.pi * k / N) for k, n in enumerate(range(half))]
    weighted_even = [even * w for even, w in zip(x_even, W)]
    begin = [x + w for x, w in zip(x_odd, weighted_even)]
    end = [x - w for x, w in zip(x_odd, weighted_even)]
    return begin + end
    
a = [0, 1, 3, 8, 0, 0, 0, 0] 
F = fft(a)
C = cooley_tukey_recursive(a)
E = list(np.fft.fft(a))
print(F)
print(E)
for i in range(len(a)):
    assert(math.isclose(abs(E[i]), abs(C[i]), abs_tol=1e-8))
