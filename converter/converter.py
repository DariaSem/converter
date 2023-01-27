from abc import ABC, abstractmethod


class Converter(ABC):
    def get_digit_list(self, string):
        return [ord(i) for i in string]

    @abstractmethod
    def convert(self, string):
        pass


class BinaryConverter(Converter):
    def convert(self, string):
        digit_list = self.get_digit_list(string)
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
    def convert(self, string):
        digit_list = self.get_digit_list(string)
        return [oct(i).replace('0o', '') for i in digit_list]


class HexadecimalConverter(Converter):
    def convert(self, string):
        digit_list = self.get_digit_list(string)
        return [hex(i).replace('0x', '') for i in digit_list]


class ConverterFactory:
    def get_converter(self, notation):
        if notation == 2:
            return BinaryConverter()
        elif notation == 8:
            return OctalConverter()
        elif notation == 16:
            return HexadecimalConverter()


converterFactory = ConverterFactory()
print(converterFactory.get_converter(2).convert('hgjgj'))
