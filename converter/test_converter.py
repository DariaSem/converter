from converter import BinaryConverter
import unittest


def start_converter(string):
    return BinaryConverter(string).convert()


class TestConverter(unittest.TestCase):
    def test_lowercase_letters_to_bin(self):
        result = start_converter('abc')
        self.assertEqual(result, ['1100001', '1100010', '1100011'])
