'''
Q1 : Write a program that can encrypt  and decrypt using the Additive Cipher (Ceaser Cipher).
'''

from __future__ import annotations
from string import ascii_letters

def encrypt(user_input: str, key: int, alphabet: str | None = None) -> str:
    """
    This function Encodes a given string with the caesar cipher and returns the encoded
    message

    Parameters:
    *   user_input: the plain-text that needs to be encoded
    *   key: the number of letters to shift the message by

    Returns:
    *   A string containing the encoded cipher-text

    """
    # Set default alphabet to lower and upper case english chars
    alpha = alphabet or ascii_letters
    #abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
   
    result = ""  # The final result string

    for character in user_input:
        if character not in alpha:
            # Append without encryption if character is not in the alphabet
            result += character
        else:
            # Get the index of the new key and make sure it isn't too large
            new_key = (alpha.index(character) + key) % len(alpha)

            # Append the encoded character to the alphabet
            result += alpha[new_key]

    return result


def decrypt(user_input: str, key: int, alphabet: str | None = None) -> str:
    """
    This function Decodes a given string of cipher-text and returns the decoded plain-text
    
    Parameters:

    *   user_input: the cipher-text that needs to be decoded
    *   key: the number of letters to shift the message backwards by to decode

    Returns:
    *   A string containing the decoded plain-text

    """
    # Turn on decode mode by making the key negative
    key *= -1

    return encrypt(user_input, key, alphabet)



if __name__ == "__main__":
    while True:
        print(f'\n{"-" * 15}\n     Menu\n{"-" * 15}')
        print(*["1. Encryption", "2. Decryption", "3. Quit"], sep="\n")

        # get user input
        choice = input("\nWhat would you like to do ?: ").strip() or "3"

        # run functions based on what the user choose
        if choice not in ("1", "2", "3"):
            print("Invalid choice, please enter a valid choice")
        elif choice == "1":
            user_input = input("\nPlease enter the Text to be encrypted: ")
            key = int(input("Please enter Shift or Key : ").strip())

            print("\nEncrypted Text is : " + encrypt(user_input, key))
        elif choice == "2":
            user_input = input("Please enter the Text to be decrypted: ")
            key = int(input("Please enter Shift or Key : ").strip())

            print("\nDecrypted Text is : " + decrypt(user_input, key))

        elif choice == "3":
            print("Bye Bye Sherlok ! ")
            break