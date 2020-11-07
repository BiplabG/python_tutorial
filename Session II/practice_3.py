"""3. Write a python program to check if a number is prime or not. 
Hint: a prime number is one which can only be exactly divided by 1 or the same number. """

number = int(input("Enter the number: \n"))

prime_flag = True
if number == 0 or number == 1:
    print("Not a prime number.")
else:
    for i in range(2, (number // 2)+1):
        if number % i == 0:
            print("Not a prime number")
            prime_flag = False
            break

    if (prime_flag):
        print(f"Number {number} is a prime number.")
