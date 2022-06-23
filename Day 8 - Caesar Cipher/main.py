alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(message, num_shift):
    encoded_text = ""

    for letter in message:
        position = alphabet.index(letter)  # will give back an integer where the index of the letter is
        new_position = position + num_shift
        if new_position > 25:
            new_position -= 25
            new_letter = alphabet[new_position - 1]
        else:
            new_letter = alphabet[new_position]

        encoded_text += new_letter

    print(f"The encoded text is {encoded_text}")


def decrypt(message, num_shift):
    decoded_text = ""

    for letter in message:
        position = alphabet.index(letter)
        new_position = position - num_shift
        new_letter = alphabet[new_position]
        decoded_text += new_letter

    print(f"The decoded text is {decoded_text}")


if direction.lower() == "encode":
    encrypt(message=text, num_shift=shift)
if direction.lower() == "decode":
    decrypt(message=text, num_shift=shift)

