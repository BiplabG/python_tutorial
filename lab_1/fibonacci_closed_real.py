import math
import numpy as np
from numpy.lib.scimath import power
import matplotlib.pyplot as plt

a = (1 + math.sqrt(5)) / 2
b = (1 - math.sqrt(5)) / 2

# array = np.sort(np.random.uniform(-5, 5, 100))
array = np.arange(-5, 5, 0.1)
print(array.shape)


def fib_closed(num):
    return (power(a, num)-power(b, num))/(a-b)


fib_closed_vectorized = np.vectorize(fib_closed)
fib_array = fib_closed_vectorized(array)
plt.plot(fib_array.imag, fib_array.real, "b-")
plt.show()
