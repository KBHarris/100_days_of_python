import random

word_list = ['ardvark', 'baboon', 'camel']

chosen_word = random.choice(word_list)
word_length = (len(chosen_word))

display = []
for char in range(word_length):
    display.append('_')

print(display)

end_of_game = False

while end_of_game == False:
    guess = input("Please guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")
