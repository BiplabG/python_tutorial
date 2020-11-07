"""5. Write a python program to check if a three digit number is palindrome or not. 
Hint: Palindrome is a number which is same when read from either left hand side or right hand side. For example: 101 or 141 or 656 etc.
"""

num = int(input("Enter the number: \n"))
if (num % 10) == (num // 100):
    print("Palindrome Number.")
else:
    print("Not a Palindrome Number.")
