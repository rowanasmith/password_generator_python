#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


final_letters = ""
final_symbols = ""
final_numbers = ""

for letter in range(0, nr_letters):
  if len(final_letters) < nr_letters:
    final_letters += letters[random.randint(0, 51)]

for symbol in range(0, nr_symbols):
  if len(final_symbols) < nr_symbols:
    final_symbols += symbols[random.randint(0, 8)]

for number in range(0, nr_numbers):
  if len(final_numbers) < nr_numbers:
    final_numbers += numbers[random.randint(0, 9)]

sorted_password = final_letters + final_symbols + final_numbers

# print(sorted_password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

shuffled_password = "".join(random.sample(sorted_password, len(sorted_password)))

print(shuffled_password)