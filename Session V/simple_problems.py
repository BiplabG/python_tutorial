"""1. Create a 1D array of numbers from 0 to 9"""
import numpy as np
print(np.arange(10))

"""2. Create a 3×3 numpy array of all True’s"""
print(np.full((3, 3), True, dtype=bool))

"""3. Extract all odd numbers from arr"""
a = np.arange(10)
a[a % 2 == 1]

"""Replace all odd numbers in arr with -1 without changing arr"""
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)

"""Reshape an array"""
arr = np.arange(12)
# print(arr.reshape((2, 6)))
print(arr.reshape((2, -1)))

"""Stack arrays a and b vertically"""
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
# np.concatenate([a,b], axis=0)
np.vstack([a, b])

"""Create the following pattern without hardcoding. 
Use only numpy functions and the below input array a."""
a = np.array([1, 2, 3])
np.concatenate([np.repeat(a, 3), np.tile(a, 3)], axis=0)

"""Convert the function maxx that works on two scalars, to work on two arrays."""


def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max = np.vectorize(maxx, otypes=[float])
pair_max(a, b)
