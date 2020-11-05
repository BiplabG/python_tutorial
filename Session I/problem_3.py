"""
    Ask a user his name, address and his hobby. Then print a statement as follows:
    You are <name>. You live in <address>. You like to do <> in your spare time.
"""

name = input("Name:\n")
address = input("Address:\n")
hobby = input("Hobby:\n")

print("You are %s. You live in %s. You like to do %s in your spare time." %(name, address, hobby))
print(f"You are {name}. You live in {address}. You like to do {hobby} in your spare time.")
