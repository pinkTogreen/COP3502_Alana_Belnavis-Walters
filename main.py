def menu():
    print(
        "Menu"
        "\n-------------"
        "\n1. Encode"
        "\n2. Decode"
        "\n3. Quit\n"

    )


def encode(password):
    enco_str = ""
    for i in password:
        if int(i) >= 7:
            num = (int(i)+3) % 10
            enco_str += str(num)
        else:
            num = int(i) + 3
            enco_str += str(num)

    return enco_str


def decode(string): # Added decoded string
    un_pass = ""
    for i in range(len(string)):
        if int(string[i]) <= 2:
            un_pass += str(int(string[i]) +7)
        else:
            un_pass += str(int(string[i]) - 3)
    print(f'The encoded password is {string}, and the original password is {un_pass}.\n')


opt = 0
password = 0

if __name__ == "__main__":

    while opt != 3:

        menu()

        try:
            opt = int(input("Please enter an option: "))
            if opt == 1:
                password = input("Please enter your password to encode: ")
                encoded_pass = encode(password)
                print('Your password has been encoded and stored!\n')
                continue

            elif opt == 2:
                decoded = decode(encoded_pass)
                continue

                # i could have just printed the password variable and the encoded pass since
                # they're both in memory but i wasn't sure
                # if we needed to use a function for both requirements

            elif opt == 3:
                break

        except ValueError:
            print('Numeric characters please.\n')
            # handles value errors if user puts in letters or symbols
