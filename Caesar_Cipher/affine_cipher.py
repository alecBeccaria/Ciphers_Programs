import re
from util import alphabet, alpha_len, regex, get_caesar_shift, get_multi_key


# encrypt with  ((index * multi_key) + caesarKey) % mod
def encrypt(key: int, message: str):
    message = message.upper()
    messageArr = [char for char in message]
    caesar_shift = get_caesar_shift(key)
    multi_key = get_multi_key(key, caesar_shift)
    print(messageArr)
    for i in range(len(messageArr)):
        letter = messageArr[i]
        nonAlpha = re.search(regex, letter)
        if (nonAlpha is None):
            alphaIndex = alphabet.index(letter)
            cipher_index = ((alphaIndex * multi_key) + caesar_shift) % alpha_len
            messageArr[i] = alphabet[int(cipher_index)]
    message = ""
    return message.join(messageArr)

# x=(multi_key_inverse * (alphaIndex - caesar_shift)) % alpha_length
def decrypt(key: int, message: str):
    message = message.upper()
    messageArr = [char for char in message]
    caesar_shift = get_caesar_shift(key)
    multi_key = get_multi_key(key, caesar_shift)
    multi_key_inverse = pow(multi_key, -1, alpha_len)
    print(messageArr)
    for i in range(len(messageArr)):
        letter = messageArr[i]
        nonAlpha = re.search(regex, letter)
        if (nonAlpha is None):
            alphaIndex = alphabet.index(letter)
            cipher_index = int((multi_key_inverse * (alphaIndex - caesar_shift)) % alpha_len)
            messageArr[i] = alphabet[cipher_index]
    message = ""
    return message.join(messageArr)
