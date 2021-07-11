import random
import hangman_words
import hangman_art


word_list = hangman_words.word_list

chosen_word = random.choice(word_list)
word_length = (len(chosen_word))

lives = 6

print(hangman_art.logo)

display = []
for char in range(word_length):
    display.append('_')

end_of_game = False



while end_of_game == False:
    guess = input("Please guess a letter: ").lower()

    if guess in display:
      print("You have already guessed that letter.")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
      print(f"{guess} is not in the hidden word.")
      lives -= 1
      if lives == 0:
        end_of_game = True
        print(f'You lose. The word was {chosen_word}.')

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    print(hangman_art.stages[lives])
