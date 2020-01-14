#!/usr/bin/python3
import pdb
import cmath
import math
import numpy as np
from matplotlib import pyplot

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

def get_next_power_of_two(n):
    return pow(2, ceil(log(x)/log(2)))

def cooley_tukey_recursive(a):
    x = a.copy()
    # Algorithm must be power of two size input
    # Padding by zero yields the same results
    if not is_power_of_two(len(x)):
        x = x + [0] * (get_next_power_of_two(n) - len(x))
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

def bitReverseOrder(X):
    N = len(X)
    nbits = math.ceil(math.log2(N))
    ans = []
    for index in range(N):
        binString = "{0:{fill}{width}b}".format(index, fill='0', width=nbits)
        newIndex = int(binString[::-1], 2)
        ans.append(X[newIndex])
    return ans

def cooley_tukey_iterative(x):
    N = len(x)

# TEST BITREVERSEORDER
print(bitReverseOrder([0, 1, 2, 3, 4, 5, 6, 7]))
