from converter import ConverterFactory
import unittest


class TestConverter(unittest.TestCase):
    def test_lowercase_letters_to_bin(self):
        result = ConverterFactory().get_converter(2).convert('abc')
        self.assertEqual(result, ['1100001', '1100010', '1100011'])

    def test_incorrect_notation(self):
        with self.assertRaises(KeyError) as cm:
            ConverterFactory().get_converter(3)
        self.assertTrue("incorrect notation 3" in str(cm.exception))



