user_attributes = {
    'name': 'Biplab',
    'age': 25,
    'address': 'Kathmandu',
    'profession': 'Engineer'
}

user_request = input("What do you want? \n")
if user_request in user_attributes:
    print(user_attributes[user_request])
else:
    print("Invalid request.")
