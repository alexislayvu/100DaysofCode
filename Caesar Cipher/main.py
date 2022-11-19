import art

print(art.logo)


def caesar(message, num_shift, cipher_direction):
    encoded_text = ""
    decoded_text = ""

    if cipher_direction == "encode":
        for letter in message:
            position = alphabet.index(letter)
            new_position = position + num_shift
            if position > 25:
                new_position -= 25
                new_letter = alphabet[new_position - 1]
            else:
                new_letter = alphabet[new_position]

            encoded_text += new_letter

        print(f"The encoded text is {encoded_text}")

    if cipher_direction == "decode":
        for letter in message:
            position = alphabet.index(letter)
            new_position = position - num_shift
            new_letter = alphabet[new_position]
            decoded_text += new_letter

        print(f"The decoded text is {decoded_text}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message=text, num_shift=shift, cipher_direction=direction)

    cont = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
    if cont == "yes":
        should_continue = True
    if cont == "no":
        should_continue = False