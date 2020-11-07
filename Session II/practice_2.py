"""2. Write a python program which checks if a number is perfect square or not. 
"""
import math
number = int(input("Enter a number to check:\n"))

square_root = math.sqrt(number)
if math.floor(square_root) == square_root:
    print(f"The number {number} is a perfect square.")
else:
    print(f"The number {number} is not a perfect square.")
