"""3. Write a python program to print first n integers. Take n input from the user. 
Hint: Use while loop doing this."""
n = int(input("Enter the number up to which you want to print the integers:"))

num = 1
while (num <= n):
    print(num)
    num = num + 1
