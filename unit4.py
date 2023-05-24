from os import system
import re
import string


counting_alpha_dict = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0,
    "J": 0,
    "K": 0,
    "L": 0,
    "M": 0,
    "N": 0,
    "O": 0,
    "P": 0,
    "Q": 0,
    "R": 0,
    "S": 0,
    "T": 0,
    "U": 0,
    "V": 0,
    "W": 0,
    "X": 0,
    "Y": 0,
    "Z": 0,
}

numbered_alpha_dict = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
}

simple_alphabet = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

rev_numbered_alpha_dict = dict(
    [(value, key) for key, value in numbered_alpha_dict.items()]
)

letterFrequencies = {
    "E": "12.2%",
    "T": "8.8%",
    "A": "7.9%",
    "O": "7.2%",
    "I": "6.8%",
    "N": "6.5%",
    "S": "6.1%",
    "H": "5.9%",
    "R": "5.8%",
    "D": "4.1%",
    "L": "3.9%",
    "C": "2.7%",
    "U": "2.7%",
    "M": "2.3%",
    "W": "2.3%",
    "F": "2.1%",
    "G": "1.9%",
    "Y": "1.9%",
    "P": "1.8%",
    "B": "1.4%",
    "V": "1.0%",
    "Z": "1.0%",
    "K": "0.8%",
    "J": "0.2%",
    "X": "0.2%",
    "Q": "0.1%",
}

letterFrequencies = list(letterFrequencies.items())


def print_freq(freq_dict: dict) -> None:
    # print("----------------------------------")
    freq_dict = dict(sorted(freq_dict.items(), key=lambda x: x[0]))
    for key, value in freq_dict.items():
        print(f"{key}: {value}")


def count_rel_freq(secret: str) -> dict:
    out_dict = {}
    cur_alpha_dict = counting_alpha_dict.copy()
    for letter in secret.upper():
        try:
            cur_alpha_dict[letter] += 1
        except KeyError:
            pass
    sorted_dict = sorted(cur_alpha_dict.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_dict:
        out_dict[item[0]] = item[1]
    return out_dict


# print_freq(count_rel_freq(str(input("Secret: "))))


def print_shifted(sec_key_tups: tuple):
    for tup in sec_key_tups:
        print(f"{tup[0]}:{tup[1]}:{shift_letter(tup[0],tup[1])}", end="|")
    print()


def shift_letter(letter: str, shift: int) -> str:
    if letter not in numbered_alpha_dict.keys():
        return letter
    return rev_numbered_alpha_dict[(numbered_alpha_dict[letter] + shift) % 26]


def vegigenere_enc(secret: str, key: str) -> str:
    secret = secret.upper()
    key_len = len(key)
    key_count = 0
    secret_key_tups: list = []
    output = ""

    for letter in secret:
        if letter not in numbered_alpha_dict.keys():
            secret_key_tups.append((letter, 0))
        else:
            secret_key_tups.append((letter, numbered_alpha_dict[key[key_count]]))
            key_count += 1
            if key_count == key_len:
                key_count = 0
    print_shifted(secret_key_tups)
    for tup in secret_key_tups:
        output += shift_letter(tup[0], tup[1])
    return output


def vegigenere_dec(secret: str, key: str) -> str:
    secret = secret.upper()
    key_len = len(key)
    key_count = 0
    secret_key_tups: list = []
    output = ""
    for letter in secret:
        if letter not in numbered_alpha_dict.keys():
            secret_key_tups.append((letter, 0))
        else:
            secret_key_tups.append((letter, 26 - numbered_alpha_dict[key[key_count]]))
            key_count += 1
            if key_count == key_len:
                key_count = 0
    print_shifted(secret_key_tups)
    for tup in secret_key_tups:
        output += shift_letter(tup[0], (tup[1]))
    return output


def frequency():
    text = split_strings()
    freq = {}
    freqPercent = {}
    messageChars = re.sub("[\W\d_]+", "", text)

    for letter in numbered_alpha_dict.keys():
        freq[letter] = 0
        for char in messageChars:
            if letter == char:
                freq[letter] += 1
        freqPercent[letter] = round((freq[letter] / len(messageChars)) * 100, 3)

    sortedPercent = sorted(freqPercent.items(), key=lambda x: x[1], reverse=True)
    sortedPercentList = []

    for index, letter in enumerate(sortedPercent):
        print(
            f"{letter[0]} : {letter[1]}%\t\t{letterFrequencies[index][0]} : {letterFrequencies[index][1]}"
        )
        sortedPercentList.append(list(letter))

    print(f"Sum: {len(messageChars)}")
    # replace(sortedPercentList)


def split_strings(secret: str, freq: int, start: int) -> str:
    print(f"freq: {freq}, start: {start}")
    start -= 1
    groups = [secret[i : i + freq] for i in range(0, len(secret), freq)]
    output_chars = []
    for group in groups:
        try:
            output_chars.append(group[start])
        except IndexError:
            pass
    print("".join(output_chars))
    return "".join(output_chars)


def create_freq_percent(secret: str):
    freqs = count_rel_freq(secret)
    secret_len = len(secret)
    # print(freqs)
    freq = {}
    for key, value in freqs.items():
        # print(f"{key}: {value} / {secret_len} = {round((value / secret_len), 3)}")
        freq[key] = round((value * 100 / secret_len), 1)
    return freq


def decrypt_without_key():
    secret = str(input("Secret: "))
    freq = int(input("Frequency: "))
    secret = clean_string(secret)
    key = []
    for i in range(freq):
        print("----------------------------------")
        letters = split_strings(secret, freq, i + 1)
        # print(create_freq_percent(letters))
        print_freq(count_rel_freq(letters))
        # print(list(count_rel_freq(letters).keys())[0])
        highest_key = list(count_rel_freq(letters).keys())[0]
        # print((simple_alphabet.index(highest_key) - simple_alphabet.index("E")) % 26)
        new_key = simple_alphabet[
            (simple_alphabet.index(highest_key) - simple_alphabet.index("E")) % 26
        ]
        print(f"Suggested Key: {new_key}")
        key.append(new_key)
    print("----------------------------------")
    print("".join(key))


def clean_string(secret: str) -> str:
    return re.sub("[\W\d_]+", "", secret).upper()


def monoalphabetic_decrypt():
    ciphertext = input("Enter a message to decrypt: ")
    key = input("Enter a key: ")

    # Convert the key to uppercase
    key = key.upper()
    key = re.sub(r"[\W_]", "", key)

    # Remove duplicate characters and create a set
    unique_letters = list(set(key))

    # Sort the unique letters based on the order in the key
    unique_letters.sort(key=lambda x: key.index(x))

    # Pad the list with remaining alphabet letters
    remaining_letters = list(set(string.ascii_uppercase) - set(key))
    remaining_letters.sort()
    array = unique_letters + remaining_letters[: max(0, 26 - len(unique_letters))]

    print(simple_alphabet)
    print(array)

    plaintext = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            index = array.index(ciphertext[i])
            plaintext += simple_alphabet[index]
        else:
            plaintext += ciphertext[i]
    print("Decrypted message: " + plaintext)


if __name__ == "__main__":
    # split_strings()
    # frequency()
    # print(count_rel_freq(str(input("Secret: "))))
    # quit()
    # decrypt_without_key()
    while True:
        choice = input(
            "Encrypt | Decrypt | DecryptWthoutKey | CleanString | DecryptMono | GetFreqy ? (ec/dc/dw/cs/dm/gf) (anything else to quit): "
        )
        system("cls")
        if choice.lower() == "ec":
            print(vegigenere_enc(input("Secret: "), input("Key: ").upper()))
        elif choice.lower() == "dc":
            print(vegigenere_dec(input("Secret: "), input("Key: ").upper()))
        elif choice.lower() == "dw":
            decrypt_without_key()
        elif choice.lower() == "cs":
            print("------------------------------------------------")
            print(clean_string(input("Secret: ")))
        elif choice.lower() == "dm":
            monoalphabetic_decrypt()
        elif choice.lower() == "gf":
            print_freq(count_rel_freq(input("Secret: ")))
        else:
            break


# key = (index of letter1 - index of letter2) mod 26
