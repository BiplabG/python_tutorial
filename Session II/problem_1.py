"""Write a python program which has name, address, age and profession already set in the variables. 
Then, ask user what information they want. Then, display only that information."""
name = "Biplab Gautam"
address = "Kathmandu"
age = 24
profession = "Engineer"

information = input("What do you want? \n")
if information == "name":
    print(name)
elif information == "address":
    print(address)
elif information == "age":
    print(age)
elif information == "profession":
    print(profession)
else:
    print("Are you stupid or what?")
