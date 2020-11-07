"""7. Write a program that accepts a sentence and calculate the number of
letters and digits."""

string = input("Enter the string: ")

num_letters = 0
num_digits = 0
for char in string:
    if char.isalpha():
        num_letters += 1
    elif char.isnumeric():
        num_digits += 1

print(
    f"The number of letters is {num_letters} and number of digits is {num_digits} in the string.")
