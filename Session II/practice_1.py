"""1. Write a python program to check if a number is multiple of 7 or not. 
"""

num = int(input("Enter the number please: \n"))

if (num % 7 == 0):
    print(f"The number {num} is a multiple of 7.")
else:
    print(f"The number {num} is not a multiple of 7.")
