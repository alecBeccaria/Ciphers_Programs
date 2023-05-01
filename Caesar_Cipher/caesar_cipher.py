import re
from util import alphabet, alpha_len, regex


# encrypt with  (index + key) % 26
def encrypt(key: int, message: str):
    message = message.upper()
    messageArr = [char for char in message]
    print(messageArr)
    for i in range(len(messageArr)):
        letter = messageArr[i]
        nonAlpha = re.search(regex, letter)
        if (nonAlpha is None):
            alphaIndex = alphabet.index(letter)
            cipher_index = (alphaIndex + key) % alpha_len
            messageArr[i] = alphabet[cipher_index]
    message = ""
    return message.join(messageArr)


# decrypt (index - key) % 26
def decrypt(key: int, message: str):
    message = message.upper()
    messageArr = [char for char in message]

    for i in range(len(messageArr)):
        letter = messageArr[i]
        nonAlpha = re.search(regex, letter)
        if (nonAlpha is None):
            alphaIndex = alphabet.index(letter)
            cipher_index = (alphaIndex - key) % alpha_len
            messageArr[i] = alphabet[cipher_index]
    message = ""
    return message.join(messageArr)


def brute_force(message: str):
    results: list = []
    for i in range(2, alpha_len):
        result = decrypt(i, message)
        results.append(f'message: "{result}"\nshift: {i}\n')
    return results
