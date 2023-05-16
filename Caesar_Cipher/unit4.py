import openpyxl
import os

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def guessing_letters():
    input_string = input("Enter a string: ").upper()

    # Load the Excel workbook
    workbook = openpyxl.load_workbook('TestSheet.xlsx')

    # Select the worksheet where you want to write the data
    worksheet = workbook['Sheet1']

    # Write the data to column B starting from row 2 to row 27
    for i, letter in enumerate(alphabet):
        count = input_string.count(letter)
        cell = worksheet.cell(row=i+2, column=2)
        cell.value = count

    # Save the changes to the Excel file
    workbook.save('TestSheet.xlsx')
    os.startfile('TestSheet.xlsx')

    while True:
        letter_to_replace = input("Enter the letter to replace: ")
        if letter_to_replace == "0":
            break
        letter_to_replace_with = input("Enter the letter to replace with: ")

        input_string = input_string.replace(letter_to_replace, letter_to_replace_with)

        print()
        print(input_string)
        print()


def encrypt_vigenere():
    plaintext = input("Enter a message to encrypt: ")
    key = input("Enter a key: ").upper()

    chart = [[0 for i in range(26)] for j in range(26)]
    for i in range(26):
        for j in range(26):
            chart[i][j] = chr((i+j) % 26 + ord('A'))
    
    # Convert the plaintext and key to uppercase
    plaintext = plaintext.upper()
    key = key.upper()
    
    ciphertext = ""
    key_index = 0
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            row = ord(key[key_index % len(key)]) - ord('A')
            col = ord(plaintext[i]) - ord('A')
            ciphertext += chart[row][col]
            key_index += 1
        else:
            ciphertext += plaintext[i]
    
    print("Encrypted message: " + ciphertext)


def decrypt_vigenere():
    ciphertext = input("Enter a message to decrypt: ")
    key = input("Enter a key: ").upper()

    ciphertext = ciphertext.upper()

    chart = [[0 for i in range(26)] for j in range(26)]
    for i in range(26):
        for j in range(26):
            chart[i][j] = chr((i+j) % 26 + ord('A'))
    
    # Decrypt the ciphertext using the Vigenere Cipher chart and the key
    plaintext = ""
    key_index = 0
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            row = ord(key[key_index % len(key)]) - ord('A')
            col = chart[row].index(ciphertext[i])
            plaintext += chr(col + ord('A'))
            key_index += 1
        else:
            plaintext += ciphertext[i]
    
    print("Decrypted message: " + plaintext)


def brute_forse_vigenere():
    ciphertext = input("Enter a message to decrypt: ").upper()

    chart = [[0 for i in range(26)] for j in range(26)]
    for i in range(26):
        for j in range(26):
            chart[i][j] = chr((i+j) % 26 + ord('A'))
    

