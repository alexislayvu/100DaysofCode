"""
Day 5 - Password Generator
Alexis Lay Vu
"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = ''

for i in range(num_letters):
    password += random.choice(letters)

for j in range(num_symbols):
    password += random.choice(symbols)

for k in range(num_numbers):
    password += random.choice(numbers)

# Shuffle the order of the characters in the string (https://note.nkmk.me/en/python-random-shuffle/)
shuffle_password = ''.join(random.sample(password, len(password)))
print("Here is your password:", shuffle_password)
