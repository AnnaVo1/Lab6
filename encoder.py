# Anna Vo

# Takes in a string 8-digit password and returns the encoded password as another 8-digit string
def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = int(digit) + 3
        # If the new digit is 10 or greater, subtract 10 from the new digit
        if new_digit >= 10:
            new_digit -= 10
        encoded_password += str(new_digit)
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

#Decode Function by partner - Bryan Gomez
def decode(string):
    #The decode function works by creating an empty list and interating through the digits of the string that's entered.
    decoded_string = []
    for x in range(0, len(string)):
        current_num = int(string[x])
        #In this simple encryption program we simply return the value of the number
        if current_num >= 3:
            new_num = str(current_num - 3)
        elif current_num <= 2:
            new_num = str(current_num + 7)
        #After the function processes each number in the string it appends all of the components to the empty list created earlier.
        decoded_string.append(new_num)
    #All portions of the list are concatenated into one string.
    return ''.join(decoded_string)

if __name__ == '__main__':
    main()
