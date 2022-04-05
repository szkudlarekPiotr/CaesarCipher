from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
    end_word = ''
    shift = shift % 26

    for letter in text:
        if letter in alphabet:
            if direction == 'encode':
                end_word += alphabet[alphabet.index(letter) + shift]
            elif direction == 'decode':
                end_word += alphabet[alphabet.index(letter) - shift]
        else:
            end_word += letter
    print(f"Your {direction}d message is {end_word}")


print(logo)
end_program = False

while not end_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    restart = input('Do you want to restart the program?\n')
    if restart == 'no':
        end_program = True
        print("Goodbye")
