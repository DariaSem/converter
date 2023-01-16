def converter(string, notation):
    string_to_digit = [ord(i) for i in string]
    if notation == 2:
        new_string = ''.join(bin(i) for i in string_to_digit).replace('0b', '')
    elif notation == 16:
        new_string = ''.join(hex(i) for i in string_to_digit).replace('0x', '')
    elif notation == 8:
        new_string = ''.join(oct(i) for i in string_to_digit).replace('0o', '')
    return new_string


print(converter('Hello', 2))
