def is_valid_binary(bin_num):
    return all(char in "01." for char in bin_num)


def is_valid_decimal(dec_num):
    return all(char in "0123456789." for char in dec_num)


def is_valid_octal(oct_num):
    return all(char in "01234567." for char in oct_num)


def is_valid_hexa(hex_num):
    return all((char in "0123456789abcdefABCDEF." or char == "-") for char in hex_num)


def binary_to_x(bin_num):
    if bin_num[0] == "-":
        bin_num = bin_num[1:]
        is_negative = True
    else:
        is_negative = False

    if "." in bin_num:
        whole, fraction = bin_num.split(".")
        decimal_whole = int(whole, 2)
        decimal_fraction = int(fraction, 2) / (2 ** len(fraction))
    else:
        decimal_whole = int(bin_num, 2)
        decimal_fraction = 0

    decimal = decimal_whole + decimal_fraction
    if is_negative:
        decimal = -decimal

    hexa = hex(int(decimal_whole))[2:]
    octal = oct(int(decimal_whole))[2:]

    return decimal, hexa, octal


def decimal_to_x(dec_num):
    if dec_num[0] == "-":
        dec_num = dec_num[1:]
        is_negative = True
    else:
        is_negative = False

    if "." in dec_num:
        whole, fraction = dec_num.split(".")
        decimal_whole = int(whole)
        decimal_fraction = int(fraction) / (10 ** len(fraction))
    else:
        decimal_whole = int(dec_num)
        decimal_fraction = 0

    decimal = decimal_whole + decimal_fraction
    if is_negative:
        decimal = -decimal

    binary = bin(int(decimal_whole))[2:]
    hexa = hex(int(decimal_whole))[2:]
    octal = oct(int(decimal_whole))[2:]

    return binary, hexa, octal


def octal_to_x(oct_num):
    if oct_num[0] == "-":
        oct_num = oct_num[1:]
        is_negative = True
    else:
        is_negative = False

    if "." in oct_num:
        whole, fraction = oct_num.split(".")
        decimal_whole = int(whole, 8)
        decimal_fraction = int(fraction, 8) / (8 ** len(fraction))
    else:
        decimal_whole = int(oct_num, 8)
        decimal_fraction = 0

    decimal = decimal_whole + decimal_fraction
    if is_negative:
        decimal = -decimal

    binary = bin(int(decimal_whole))[2:]
    hexa = hex(int(decimal_whole))[2:]

    return binary, decimal, hexa


def hexa_to_x(hex_num):
    if hex_num[0] == "-":
        hex_num = hex_num[1:]
        is_negative = True
    else:
        is_negative = False

    if "." in hex_num:
        whole, fraction = hex_num.split(".")
        decimal_whole = int(whole, 16)
        decimal_fraction = int(fraction, 16) / (16 ** len(fraction))
    else:
        decimal_whole = int(hex_num, 16)
        decimal_fraction = 0

    decimal = decimal_whole + decimal_fraction
    if is_negative:
        decimal = -decimal

    binary = bin(int(decimal_whole))[2:]
    octal = oct(int(decimal_whole))[2:]

    return binary, decimal, octal


def binary_to_decimal(binary):
    is_negative = binary[0] == "-"
    binary = binary.lstrip("-")

    whole, fraction = binary.split(".") if "." in binary else (binary, None)
    result = int(whole, 2) + (int(fraction, 2) / 2 ** len(fraction) if fraction else 0)

    return -result if is_negative else result


def decimal_to_binary(number, num_bits=None):
    is_negative = number < 0
    number = abs(number)

    whole = bin(int(number))[2:]
    fraction = number - int(number)

    fraction_bin = ""
    while fraction:
        fraction *= 2
        bit = int(fraction)
        fraction -= bit
        fraction_bin += str(bit)

    result = whole + ("." + fraction_bin if fraction_bin else "")

    if is_negative:
        result = "".join("1" if bit == "0" else "0" for bit in result)
        result = decimal_to_binary(binary_to_decimal(result) + 1)

    if num_bits is not None:
        result = result.zfill(num_bits)

    return result


def binary_operations():
    while True:
        print("Menu-2 (Binary Operations)")
        print("[1] Division")
        print("[2] Multiplication")
        print("[3] Subtraction")
        print("[4] Addition")
        print("[5] Negative (2's Complement)")
        print("[6] Exit")

        choice = int(input("Enter your choice: "))
        if choice == 6:
            print("Exiting program.")
            break
        elif choice < 1 or choice > 5:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

        num1 = input("Enter the first binary number: ")
        num1_dec = binary_to_decimal(num1)

        if choice != 5:
            num2 = binary_to_decimal(input("Enter the second binary number: "))
            num_bits = None
        else:
            num2 = None
            num_bits = len(num1)

        if choice == 1:
            result = num1_dec / num2
        elif choice == 2:
            result = num1_dec * num2
        elif choice == 3:
            result = num1_dec - num2
        elif choice == 4:
            result = num1_dec + num2
        elif choice == 5:
            result = -num1_dec

        print("The result is: ", decimal_to_binary(result, num_bits))


def number_system_conversion():
    while True:
        print("Menu-3 (Conversion)")
        print("[1] Binary to X")
        print("[2] Decimal to X")
        print("[3] Octal to X")
        print("[4] Hexa to X")
        print("[5] Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            while True:
                bin_num = input("Input Binary: ")
                if is_valid_binary(bin_num):
                    decimal, hexa, octal = binary_to_x(bin_num)
                    print(f"Output:\nDecimal: {decimal}\nHexa: {hexa}\nOctal: {octal}")
                    break
                else:
                    print(
                        "Invalid binary number. A binary number should only contain 0s and 1s. For example: 1010."
                    )
        elif choice == "2":
            while True:
                dec_num = input("Input Decimal: ")
                if is_valid_decimal(dec_num):
                    binary, hexa, octal = decimal_to_x(dec_num)
                    print(f"Output:\nBinary: {binary}\nHexa: {hexa}\nOctal: {octal}")
                    break
                else:
                    print(
                        "Invalid decimal number. A decimal number should only contain digits from 0 to 9. For example: 1234."
                    )
        elif choice == "3":
            while True:
                oct_num = input("Input Octal: ")
                if is_valid_octal(oct_num):
                    binary, decimal, hexa = octal_to_x(oct_num)
                    print(
                        f"Output:\nBinary: {binary}\nDecimal: {decimal}\nHexa: {hexa}"
                    )
                    break
                else:
                    print(
                        "Invalid octal number. An octal number should only contain digits from 0 to 7. For example: 123."
                    )
        elif choice == "4":
            while True:
                hex_num = input("Input Hexa: ")
                if is_valid_hexa(hex_num):
                    binary, decimal, octal = hexa_to_x(hex_num)
                    print(
                        f"Output:\nBinary: {binary}\nDecimal: {decimal}\nOctal: {octal}"
                    )
                    break
                else:
                    print(
                        "Invalid hexadecimal number. A hexadecimal number should only contain digits from 0 to 9 and letters from A to F (case-insensitive). For example: 1A3F."
                    )
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please choose a valid option.")


def main_menu():
    while True:
        print("Menu-1 (Main Menu)")
        print("[1] Binary Operations")
        print("[2] Number System Conversion")
        print("[3] Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            binary_operations()
        elif choice == "2":
            number_system_conversion()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


main_menu()
