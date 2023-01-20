from abc import ABC, abstractmethod


class Converter(ABC):
    def __init__(self, string):
        self.string = string

    def get_digit_list(self):
        return [ord(i) for i in self.string]

    @abstractmethod
    def convert(self):
        pass


class BinaryConverter(Converter):
    def convert(self):
        digit_list = self.get_digit_list()
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


class OctalConverter(Converter):
    def convert(self):
        digit_list = self.get_digit_list()
        return [oct(i).replace('0o', '') for i in digit_list]


class HexadecimalConverter(Converter):
    def convert(self):
        digit_list = self.get_digit_list()
        return [hex(i).replace('0x', '') for i in digit_list]


class Notation:
    def __init__(self, string, notation):
        self.string = string
        self.notation = notation

    def choose_converter(self):
        if self.notation == 2:
            return BinaryConverter(self.string).convert()
        elif self.notation == 8:
            return OctalConverter(self.string).convert()
        elif self.notation == 16:
            return HexadecimalConverter(self.string).convert()


def converter(string, notation):
    return Notation(string, notation).choose_converter()


