import re
from util import alphabet, alpha_len, regex


# encrypt with  (KeyLetterIndex + PlainLetterIndex) % 26
def encrypt(key: str, message: str):
    message = message.upper()
    key = key.replace(' ', '')
    key = key.upper()
    messageArr = [char for char in message]
    key_arr = [char for char in key]
    key_len = len(key)
    print(messageArr)
    key_index = 0
    for i in range(len(messageArr)):
        letter = messageArr[i]
        key_letter = key_arr[key_index]
        nonAlpha = re.search(regex, letter)
        if (nonAlpha is None):
            alphaIndex = alphabet.index(letter)
            keyIndex = alphabet.index(key_letter)
            cipher_index = (alphaIndex + keyIndex) % alpha_len
            messageArr[i] = alphabet[cipher_index]
            key_index += 1
            if (key_index >= key_len):
                key_index = 0
    message = ""
    return message.join(messageArr)


# decrypt (index - key) % 26
def decrypt(key: str, message: str):
    message = message.upper()
    key = key.replace(' ', '')
    key = key.upper()
    messageArr = [char for char in message]
    key_arr = [char for char in key]
    key_len = len(key)
    print(messageArr)
    key_index = 0
    for i in range(len(messageArr)):
        letter = messageArr[i]
        key_letter = key_arr[key_index]
        nonAlpha = re.search(regex, letter)
        if (nonAlpha is None):
            alphaIndex = alphabet.index(letter)
            keyIndex = alphabet.index(key_letter)
            cipher_index = ((alphaIndex - keyIndex) + 26) % alpha_len
            messageArr[i] = alphabet[cipher_index]
            key_index += 1
            if (key_index >= key_len):
                key_index = 0
    message = ""
    return message.join(messageArr)


def brute_force(message: str):
    results: list = []
    for i in range(2, alpha_len):
        result = decrypt(i, message)
        results.append(f'message: "{result}"\nshift: {i}\n')
    return results
