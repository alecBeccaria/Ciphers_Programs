import caesar_cipher as caesar
import multiplicitive_cipher as multi
import affine_cipher as affine
import util


def main():
    print('--------------------------------------------------')
    exit = False
    while (exit is False):
        print()
        print('---- Main Menu ----')
        print("1. Caesar Cipher\n2. Multiplicitive Cipher\n3. Affine Cipher\n4. Tools\n type 'exit' to exit")
        selection = input("Select Menu Option: ")
        back = False
        print()
        if (selection == '1'):
            while (back is False):
                print("---- Caesar Cipher ----")
                print("1. Encrypt Message\n2. Decrypt Message\n3. Print Key\n type 'back' to go back")
                selection = input("Select Menu Option: ")
                message: str
                key: int
                # Encrypt message
                if (selection == '1'):
                    message = input("Enter a message to ecrypt: ")
                    key = int(input('Enter a key to shift by: '))
                    result = caesar.encrypt(key, message)
                    print(result)
                # decrypt message
                elif (selection == '2'):
                    message = input("Enter message to decrypt: ")
                    key = int(input('Enter a key to shift by: '))
                    result = caesar.decrypt(key, message)
                    print(result)
                # Print out key
                elif (selection == '3'):
                    key = int(input('Enter a key to shift by: '))
                    util.print_alphabet_key(key, 'caesar')
                # exit program
                elif (selection == 'back'):
                    back = True
                else:
                    print('Not a valid selection!')
        elif (selection == '2'):
            while (back is False):
                print("---- Multiplicitive Cipher ----")
                print("1. Encrypt Message\n2. Decrypt Message\n3. Print Key\n type 'back' to go back")
                selection = input("Select Menu Option: ")
                message: str
                key: int
                # Encrypt message
                if (selection == '1'):
                    message = input("Enter a message to ecrypt: ")
                    good_key = False
                    while (good_key is False):
                        key = int(input('Enter a key to multiply by: '))
                        good_key = util.check_key(key)
                        if (good_key):
                            result = multi.encrypt(key, message)
                            print(result)
                        else:
                            print("Key shares common factors with 26!")
                # decrypt message
                elif (selection == '2'):
                    message = input("Enter message to decrypt: ")
                    good_key = False
                    while (good_key is False):
                        key = int(input('Enter a key to multiply by: '))
                        good_key = util.check_key(key)
                        if (good_key):
                            result = multi.decrypt(key, message)
                            print(result)
                        else:
                            print("Multi key shares factors with 26 or is > 26")
                # Print out key
                elif (selection == '3'):
                    good_key = False
                    while (good_key is False):
                        key = int(input('Enter a key to multiply by: '))
                        good_key = util.check_key(key)
                        if (good_key):
                            util.print_alphabet_key(key, 'multi')
                        else:
                            print("Multi key shares factors with 26 or is > 26")
                # exit program
                elif (selection == 'back'):
                    back = True
                else:
                    print('Not a valid selection!')
        elif (selection == '3'):
            while (back is False):
                print("---- Affine Cipher ----")
                print("1. Encrypt Message\n2. Decrypt Message\n3. Print Key\n type 'back' to go back")
                selection = input("Select Menu Option: ")
                message: str
                key: int
                # Encrypt message
                if (selection == '1'):
                    message = input("Enter a message to ecrypt: ")
                    key = int(input('Enter a key to encrypt with: '))
                    result = affine.encrypt(key, message)
                    print(result)
                # decrypt message
                elif (selection == '2'):
                    message = input("Enter message to decrypt: ")
                    key = int(input('Enter a key to decrypt with: '))
                    result = affine.decrypt(key, message)
                    print(result)
                # Print out key
                elif (selection == '3'):
                    key = int(input('Enter a key to shift by: '))
                    util.print_alphabet_key(key, 'affine')
                # exit program
                elif (selection == 'back'):
                    back = True
                else:
                    print('Not a valid selection!')
        elif (selection == '4'):
            while (back is False):
                print("---- Tools ----")
                print("1. Check Multi Key\n2. Find Multi Key Inverse\n3. Calculate Affine Key", end='')
                print("\n4. List Modulo 26 inverse pairs\n type 'back' to go back")
                selection = input("Select Menu Option: ")
                # Check Key
                if (selection == '1'):
                    key = int(input('Enter a key to check: '))
                    is_good = util.check_key(key)
                    print(f'\nGood Key: {is_good}\n')
                # Find multi key inverse
                elif (selection == '2'):
                    good_key = False
                    while (good_key is False):
                        key = int(input('Enter a key: '))
                        good_key = util.check_key(key)
                        if (good_key):
                            inverse = util.get_multi_key_inverse(key)
                            print(f'\nKey: {key}\nInverse: {inverse}\n')
                        else:
                            print("Multi key shares factors with 26 or is > 26")
                # Calc affine key
                elif (selection == '3'):
                    caesar_key = input('Enter Caesar Key: ')
                    good_key = False
                    while (good_key is False):
                        multi_key = input('Enter Multi Key: ')
                        good_key = util.check_key(int(multi_key))
                        if (good_key):
                            affine_key = util.get_affine_key(int(caesar_key), int(multi_key))
                            print(f'\nAffine Key: {affine_key}\n')
                        else:
                            print('Multi key shares factors with 26 or is > 26')
                # List Modulo 26 inverse pairs
                elif (selection == '4'):
                    util.print_inverse_pairs()
                elif (selection == 'back'):
                    back = True
                else:
                    print('Not a valid selection!')
        elif (selection == 'exit'):
            exit = True
        else:
            print('not a valid input!')


if __name__ == "__main__":
    main()
