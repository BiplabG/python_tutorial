"""4. Write a python program to print first n fibonacci sequence. Take n input from the user. 
Hint: A fibonacci sequence follows this rule: F(n+1) = F(n) + F(n-1) where first two numbers are 0 and 1 of the sequence. 
0 1 1 2 3 5 8 13 ..."""

num = int(input("Enter the number you want fibonacci sequence up to: \n"))

a = 0
b = 1
for i in range(0, num):
    print(a)
    c = a + b
    a = b
    b = c
