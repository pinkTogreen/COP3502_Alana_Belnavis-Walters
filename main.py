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


def decode(encoded):
    decoded_str = ""
    for i in encoded:
        if int(i) < 3:
            num = int(i) + 7
            decoded_str += str(num)
        else:
            num = int(i) - 3
            decoded_str += str(num)
    return decoded_str


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
                print(f"Your encoded password is {encoded_pass}, and your original password is {decoded}.")
                continue

                # i could have just printed the password variable and the encoded pass since
                # they're both in memory but i wasn't sure
                # if we needed to use a function for both requirements

            elif opt == 3:
                break

        except ValueError:
            print('Numeric characters please.\n')
            # handles value errors if user puts in letters or symbols
