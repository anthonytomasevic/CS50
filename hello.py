# Initializes name while requesting input, removing excess spaces, and title-casing name
name = input("What's your name? ").strip().title()

# Splits name into first and last name
first, last = name.split(" ")

"""
Greeting the user rather politely
"""
print(f"Hello, {first}.")