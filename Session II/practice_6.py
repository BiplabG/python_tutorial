"""6. Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a
single line."""


def extract_digits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num = num // 10
    return digits


even_nums = []
for num in range(1000, 3000 + 1):
    digits = extract_digits(num)
    flag = True
    for d in digits:
        if (d % 2 != 0):
            flag = False
    if flag:
        even_nums.append(num)

print(str(even_nums)[1:-1])
