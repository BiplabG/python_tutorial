import math

a = (1 + math.sqrt(5)) / 2
b = (1 - math.sqrt(5)) / 2

num = int(input("Enter the n value:\n"))
print(int((a**num-b**num)/(a-b)))
