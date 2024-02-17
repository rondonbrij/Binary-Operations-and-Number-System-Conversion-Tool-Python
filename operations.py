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

        print(
            "The result is: ",
            decimal_to_binary(result, num_bits),
            "in binary or",
            result,
            "in decimal",
        )


binary_operations()
