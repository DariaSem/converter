import unittest
from fibonacci import fibonacci_function, fibonacci_sequence


class FibonacciTest(unittest.TestCase):
    def test_fibonacci_to_1(self):
        result = fibonacci_function(1)
        self.assertEqual(1, result)

    def test_fibonacci_to_10(self):
        result = fibonacci_function(10)
        self.assertEqual(55, result)

    def test_fibonacci_to_100(self):
        result = fibonacci_function(100)
        self.assertEqual(354224848179261915075, result)
