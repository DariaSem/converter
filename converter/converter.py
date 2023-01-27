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
    def __init__(self):
        self.__converters = {
            2: BinaryConverter(),
            8: OctalConverter(),
            16: HexadecimalConverter(),
        }

    def get_converter(self, notation):
        if notation in self.__converters.keys():
            return self.__converters[notation]
        else:
            raise KeyError(f'incorrect notation {notation}')


converterFactory = ConverterFactory()
print(converterFactory.get_converter(3).convert('jhg'))
