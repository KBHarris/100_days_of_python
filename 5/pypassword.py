import random
letters = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

chosen_password = []

for num in range(0, nr_letters):
    chosen_password += random.choice(letters)

for num in range(0, nr_numbers):
    chosen_password += random.choice(numbers)

for num in range(0, nr_symbols):
    chosen_password += random.choice(symbols)

random.shuffle(chosen_password)

randomized_password = ''

for char in chosen_password:
    randomized_password += char

print(randomized_password)