from art import logo

alphabet = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(logo)

go_again = False

def caesar(direction, text, shift):
    output_text = ''
    for letter in text:
        if letter not in alphabet:
            output_text += letter
        else:
            position = alphabet.index(letter)
            if direction == 'encode':
                new_position = position + shift
            if direction == 'decode':
                new_position = position - shift
            new_letter = alphabet[new_position]
            output_text += new_letter
    print(f"The {direction}d text is {output_text}")
    
while not go_again:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt':\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("type the shift number: "))

    shift = shift % 26

    caesar(direction, text, shift)

    run = input("Would you like to run the cipher again? Y or N? ")
    if run.lower() == 'n':
        go_again = True