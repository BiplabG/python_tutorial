"""4. Write a python program which prints cube numbers less than a certain number provided by the user. 
"""

num = int(input("Enter the number:"))

counter = 0
while (counter ** 3 <= num):
    print(counter ** 3)
    counter = counter + 1
