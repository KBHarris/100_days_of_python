import random

word_list = ['ardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)

display = []
for char in chosen_word:
    display.append('_')

print(display)

while display.count("_") > 0:
    guess = input("Please guess a letter: ").lower()

    for char in chosen_word:
        if guess == char:
            pos = chosen_word.index(char)
            display[pos] = char
            print(display)


