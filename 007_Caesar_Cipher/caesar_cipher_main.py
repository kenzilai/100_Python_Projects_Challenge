from caesar_cipher_art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(entered_text, shift_amount):
    modified_text = ""
    if direction == "decode":
        shift_amount *= -1
    for characters in entered_text:
        if characters in alphabet:
            position = alphabet.index(characters)
            shifted_position = position + shift_amount
            modified_text += alphabet[shifted_position]
        else:
            modified_text += characters
    print(f"The {direction} text is {modified_text}.")

end_program = True
while end_program:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar_cipher(entered_text = text, shift_amount = shift)

    restart = input("Do you want to continue? Y/N\n").lower()

    if restart == "n":
        end_program = False
        print("The program is ended.")