from math import gcd


alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha_len = len(alphabet)
regex = "[\\W_]+"


def calculate_caesar_alphabet(key: int, cipher_alphabet: list):
    for i in range(alpha_len):
        cipher_index = (i + key) % alpha_len
        cipher_alphabet.append(alphabet[cipher_index])
    return cipher_alphabet


def calculate_multi_alphabet(key: int, cipher_alphabet: list):
    for i in range(alpha_len):
        cipher_index = (i * key) % alpha_len
        cipher_alphabet.append(alphabet[cipher_index])
    return cipher_alphabet


def calculate_affine_alphabet(key: int, cipher_alphabet: list):
    caesar_shift = get_caesar_shift(key)
    multi_key = get_multi_key(key, caesar_shift)
    for i in range(alpha_len):
        cipher_index = ((i * multi_key) + caesar_shift) % alpha_len
        cipher_alphabet.append(alphabet[cipher_index])
    return cipher_alphabet


def print_caesar_index(key: int):
    for i in range(alpha_len):
        cipher_index = (i + key) % alpha_len
        if (cipher_index < 10):
            print(f"0{str(cipher_index)} ", end='')
        else:
            print(f"{str(cipher_index)} ", end='')

def print_multi_index(key: int):
    for i in range(alpha_len):
        cipher_index = (i * key) % alpha_len
        if (cipher_index < 10):
            print(f"0{str(cipher_index)} ", end='')
        else:
            print(f"{str(cipher_index)} ", end='')


def print_affine_index(key: int):
    caesar_shift = get_caesar_shift(key)
    multi_key = get_multi_key(key, caesar_shift)
    for i in range(alpha_len):
        cipher_index = ((i * multi_key) + caesar_shift) % alpha_len
        if (cipher_index < 10):
            print(f"0{str(cipher_index)} ", end='')
        else:
            print(f"{str(cipher_index)} ", end='')


def print_alphabet_key(key: int, option: str):
    cipher_alphabet = []
    if (option == 'caesar'):
        cipher_alphabet = calculate_caesar_alphabet(key, cipher_alphabet)
    elif (option == 'multi'):
        cipher_alphabet = calculate_multi_alphabet(key, cipher_alphabet)
    else:
        cipher_alphabet = calculate_affine_alphabet(key, cipher_alphabet)
    print()
    for i in range(alpha_len):
        if (i < 10):
            print(f"0{str(i)} ", end='')
        else:
            print(f"{str(i)} ", end='')
    print()
    for i in range(alpha_len):
        print(f"{alphabet[i]}  ", end='')
    print()
    for i in range(alpha_len):
        print(f"{cipher_alphabet[i]}  ", end='')
    print()
    if (option == 'caesar'):
        print_caesar_index(key)
    elif (option == 'multi'):
        print_multi_index(key)
    else:
        print_affine_index(key)
    print('\n')


def check_key(key: int):
    cf = common_factors(key)
    if (len(cf) == 1 and key < alpha_len):
        return True
    return False


def common_factors(key: int):
    n = []
    g = gcd(key, 26)
    for i in range(1, g + 1):
        if g % i == 0: 
            n.append(i)
    return n


def get_caesar_shift(key: int):
    result = key % alpha_len
    return int(result)


def get_multi_key(key: int, caesarShift: int):
    result = key - caesarShift
    result = result / alpha_len
    return int(result)


def get_multi_key_inverse(key: int):
    return pow(key, -1, alpha_len)


def get_affine_key(caesar_key: int, multi_key: int):
    return (multi_key * alpha_len) + caesar_key


def print_inverse_pairs():
    inverse_pairs = []
    nums_covered = []
    for i in range(1, alpha_len):
        if (list_contains(nums_covered, i) is False):
            good_key = check_key(i)
            if (good_key):
                inverse = get_multi_key_inverse(i)
                nums_covered.append(i)
                nums_covered.append(inverse)
                inverse_pairs.append({'base': i, 'inverse': inverse})

    for pair in inverse_pairs:
        print(f"({pair['base']}, {pair['inverse']})")


def list_contains(list: list, item):
    for list_item in list:
        if (list_item == item):
            return True
    return False
