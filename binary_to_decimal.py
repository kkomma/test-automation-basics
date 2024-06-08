def decimal_to_binary(decimal_num):
    binary_num = ""
    while decimal_num != 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num = decimal_num // 2
    return binary_num

def binary_to_decimal(binary_num):
    decimal_num = 0
    power = 0
    while binary_num != 0:
        digit = binary_num % 10
        decimal_num = decimal_num + digit * (2 ** power)
        binary_num = binary_num // 10
        power += 1
    return decimal_num

# Test the functions
decimal_num = 10
print("Original Decimal Number: ", decimal_num)
binary_num = decimal_to_binary(decimal_num)
print("Binary Number: ", binary_num)
decimal_num = binary_to_decimal(int(binary_num))
print("Back to Decimal Number: ", decimal_num)