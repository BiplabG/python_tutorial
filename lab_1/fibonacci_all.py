"""Write a Python function that returns the N-th element of the sequence. 
There are at least two ways to do this: one using a for or while loop; and one using a recursion (a function calling itself). Try to write both (ask when you are stuck!). 
Compare execution time of both routines for N = 5, N = 15, N = 25 and N = 35. 
To determine execution time, you will want to use timeit in Python. What is happening and why?"""

# Note: Fibonacci Series: 0 1 1 2 3 5 8 13 ...
# Indexing for this begins from 0 as: 0 1 2 3 4 5 6 7 ...


def fibonacci_while_loop(num):
    a = 0
    b = 1
    while (num > 0):
        c = a + b
        a = b
        b = c
        num -= 1
    return a


def fibonacci_for_loop(num):
    a = 0
    b = 1
    for i in range(0, num):
        c = a + b
        a = b
        b = c
    return a


def fibonacci_recursion(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_recursion(num-1) + fibonacci_recursion(num-2)


print(fibonacci_recursion(4))
