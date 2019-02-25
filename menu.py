import sys
import os
import time
from file_algorithm import open_file_handler, key_gen_f, run_file_encryption, run_file_decryption
from plaintext_algorithm import user_input_handler, key_gen_p, encryption_and_permutation, decryption_and_permutation

# Main definition - constants
menu_actions = {}


# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')
    print("\nMatrix Encryption Simulator - inspired by Hill, AES and Feistel Cipher.")
    print("\nControls:  Type numbers from the menu below.")
    print("\nMenu")
    print("1. Plaintext encryption")
    print("2. File encryption")
    print("3. About")
    # print("4. Help")
    print("0. Exit")
    choice = input("\nMenu choice :  ")
    exec_menu(choice)

    return


# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return


# Menu 1
def menu1():
    print("\nLoaded plaintext encryption algorithm.\n")
    user_input_handler()
    key_gen_p()
    time.sleep(1)
    encryption_and_permutation()
    decryption_and_permutation()
    print("\nMenu")
    print("9. Back")
    print("0. Quit")
    choice = input("\nMenu choice :  ")
    exec_menu(choice)
    return


# Menu 2
def menu2():
    print("\nLoaded file encryption algorithm.\n")
    open_file_handler()
    key_gen_f()
    run_file_encryption()
    run_file_decryption()
    print("\nFile saved to same directory as this cipher.", "\n\nClosing Cipher. Check cipher directory for results.")


# Menu 3
def menu3():
    print("\nAuthor - Jacob Dent.\n")
    print("\n\nRepo : https://github.com/jakedent/Matrix-Encryption/blob/master/README.md\n")
    print("\nMenu")
    print("9. Back")
    print("0. Quit")
    choice = input("\nMenu choice :  ")
    exec_menu(choice)
    return


# Menu 4
def menu4():
    print("\nHelp - how to use this CLI app.\n")
    print("\n\nComing soon...\n")
    print("\nMenu")
    print("9. Back")
    print("0. Quit")
    choice = input("\nMenu choice :  ")
    exec_menu(choice)
    return


# Back to main menu
def back():
    menu_actions['main_menu']()


# Exit program
def exit_app():
    sys.exit()


# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    # '4': menu4,
    '9': back,
    '0': exit_app,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
