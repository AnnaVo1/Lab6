# Anna Vo

# Takes in a string 8-digit password and returns the encoded password as another 8-digit string
def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_password += str(int(digit) + 3)
    return encoded_password

# Prints menu
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode\n2. Decode\n3. Quit\n")

def main():
    encoded_password = ""
    program_continue = True
    # Main program loop, keeps running until user selects the exit option
    while program_continue:
        print_menu()
        user_choice = input("Please enter an option: ")
        # If user selects option 1, ask for password as input and then encode it
        if user_choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        # If user selects option 2, decode the stored encoded password
        elif user_choice == "2":
            # *** Once the decode function is written, the following 2 lines should be uncommented and the pass command should be removed ***
            # decoded_password = decode(encoded_password)
            # print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.\n")
            pass
        # If user selects option 3, exit the program loop
        elif user_choice == "3":
            program_continue = False


if __name__ == '__main__':
    main()