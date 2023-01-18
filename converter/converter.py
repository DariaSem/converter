class BinaryConverter:
    def __init__(self, string):
        self.string = string

    def convert_to_bin(self):
        digit_list = [ord(i) for i in self.string]
        bin_digit = []
        for digit in digit_list:
            symbol = ''
            while True:
                symbol = str(digit % 2) + symbol
                digit = digit // 2
                if digit < 1:
                    break
            bin_digit.append(symbol)
        return bin_digit


def converter(string, notation):
    string_to_digit = [ord(i) for i in string]
    if notation == 2:
        new_string = BinaryConverter(string).convert_to_bin()
    elif notation == 16:
        new_string = ''.join(hex(i) for i in string_to_digit).replace('0x', '')
    elif notation == 8:
        new_string = ''.join(oct(i) for i in string_to_digit).replace('0o', '')
    return new_string



