from operator import indexOf

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    new_text = ""
    for letter in original_text:
        if indexOf(alphabet, letter) + shift_amount <= 25:
            # find the index, add shift_amount, look up new letter, concat in new
            new_text += alphabet[indexOf(alphabet, letter) + shift_amount]
        else:
            new_text += alphabet[indexOf(alphabet, letter) % len(alphabet)]

    print(f"Here is the encoded text: {new_text}")

encrypt(original_text=text, shift_amount=shift)
