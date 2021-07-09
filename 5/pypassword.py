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
    chosen_password += letters[random.randint(0, 25)]


for num in range(0, nr_numbers):
    chosen_password += numbers[random.randint(0, 9)]

for num in range(0, nr_symbols):
    chosen_password += symbols[random.randint(0, 8)]

randomized_password = ''

for char in range(0, len(chosen_password)):
    x = chosen_password[random.randint(0, len(chosen_password)-1)]
    chosen_password.remove(x)
    randomized_password += x
print(randomized_password)