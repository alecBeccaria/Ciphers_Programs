import caesar_cipher as caesar
import multiplicitive_cipher as multi
import affine_cipher as affine
import util
from menu import Menu

main_menu = Menu(menu_title='Main Menu', isRoot=True)
main_menu.append('Caesar Cipher')
main_menu.append('Multiplicitive Cipher')
main_menu.append('Affine Cipher')

caesar_menu = Menu(menu_title='Caesar Cipher')
caesar_menu.append("Encrypt Message")
caesar_menu.append("Decrypt Message")
caesar_menu.append("Brute Force Decrypt")
caesar_menu.append("Print Key")

multi_menu = Menu(menu_title='Multiplicitive Cipher')
multi_menu.append('Encrypt Message')
multi_menu.append('Decrypt Message')
multi_menu.append('Brute Force Decrypt')
multi_menu.append('Print Key')
multi_menu.append('Check Multi Key')
multi_menu.append('Find Multi Key Inverse')
multi_menu.append('Print Modulo 26 inverse pairs')

affine_menu = Menu(menu_title="Affine Cipher")
affine_menu.append('Encrypt Message')
affine_menu.append('Decrypt Message')
affine_menu.append('Print Key')
affine_menu.append('Calculate Affine Key')
affine_menu.append('Break Down Affine Key')

def main():
    print('--------------------------------------------------\n')
    exit = False
    while (exit is False):
        main_menu.print_menu()
        selection = input("Select Menu Option: ")
        back = False
        print()
        if (selection == '1'):
            while (back is False):
                caesar_menu.print_menu()
                selection = input("Select Menu Option: ")
                print()
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
                # Brute Force
                elif (selection == '3'):
                    message = input("Enter message to decrypt: ")
                    results = caesar.brute_force(message)
                    for result in results:
                        print(result)
                # Print out key
                elif (selection == '4'):
                    key = int(input('Enter a key to shift by: '))
                    util.print_alphabet_key(key, 'caesar')
                # exit program
                elif (selection == 'back'):
                    back = True
                else:
                    print('Not a valid selection!')
        elif (selection == '2'):
            while (back is False):
                multi_menu.print_menu()
                selection = input("Select Menu Option: ")
                print()
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
                # Brute Force
                elif (selection == '3'):
                    message = input("Enter message to decrypt: ")
                    results = multi.brute_force(message)
                    for result in results:
                        print(result)
                # Print out key
                elif (selection == '4'):
                    good_key = False
                    while (good_key is False):
                        key = int(input('Enter a key to multiply by: '))
                        good_key = util.check_key(key)
                        if (good_key):
                            util.print_alphabet_key(key, 'multi')
                        else:
                            print("Multi key shares factors with 26 or is > 26")
                # Check Multi Key
                elif (selection == '5'):
                    key = int(input('Enter a key to check: '))
                    is_good = util.check_key(key)
                    print(f'\nGood Key: {is_good}')
                # Find multi key inverse
                elif (selection == '6'):
                    good_key = False
                    while (good_key is False):
                        key = int(input('Enter a key: '))
                        good_key = util.check_key(key)
                        if (good_key):
                            inverse = util.get_multi_key_inverse(key)
                            print(f'\nKey: {key}\nInverse: {inverse}\n')
                        else:
                            print("Multi key shares factors with 26 or is > 26")
                # print inverse pairs
                elif (selection == '7'):
                    util.print_inverse_pairs()
                # exit program
                elif (selection == 'back'):
                    back = True
                else:
                    print('Not a valid selection!')
        elif (selection == '3'):
            while (back is False):
                affine_menu.print_menu()
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
                # Calc affine key
                elif (selection == '4'):
                    good_key = False
                    while (good_key is False):
                        multi_key = input('Enter Multi Key: ')
                        caesar_key = input('Enter Caesar Key: ')
                        good_key = util.check_key(int(multi_key))
                        if (good_key):
                            affine_key = util.get_affine_key(int(caesar_key), int(multi_key))
                            print(f'\nAffine Key: {affine_key}')
                        else:
                            print('Multi key shares factors with 26 or is > 26')
                # Break down Affine key
                elif (selection == '5'):
                    affine_key = int(input("Enter Affine Key: "))
                    caesar_shift = util.get_caesar_shift(affine_key)
                    multi_key = util.get_multi_key(affine_key, caesar_shift)
                    print(f"\nMulti Key: {multi_key}\nCaesar Shift: {caesar_shift}")
                # exit program
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
