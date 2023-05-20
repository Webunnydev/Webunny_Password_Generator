# "Welcome to Webunny_Password_Generator!

import random 
 
total_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
total_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
total_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


print("Welcome to Webunny_Password_Generator!")

letters= int(input("How many letters would you like?\n")) 
symbols = int(input(f"How many symbols would you like?\n"))
numbers = int(input(f"How many numbers would you like?\n"))

list = []

for char in range(1, letters+1):
    list += random.choice(total_letters)

for char in range(1, symbols+1):
    list += random.choice(total_symbols)

for char in range(1, numbers+1):
    list += random.choice(total_numbers)

password=""

random.shuffle(list)

for char in list:
    password += char

print(f"Your password is: {password}")


