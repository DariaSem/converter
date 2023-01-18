import unittest
from fibonacci import fibonacci_function, fibonacci_sequence


class FibonacciTest(unittest.TestCase):
    def test_fibonacci_to_1(self):
        self.assertEqual(1, fibonacci_function(1))

    def test_fibonacci_to_10(self):
        self.assertEqual(55, fibonacci_function(10))

    def test_fibonacci_to_100(self):
        self.assertEqual(354224848179261915075, fibonacci_function(100))


class FibonacciSequenceTest(unittest.TestCase):
    def test_sequence_to_1(self):
        self.assertEqual(1, fibonacci_sequence(1))

    def test_sequence_to_7(self):
        self.assertEqual([1, 1, 2, 3, 5, 8, 13], fibonacci_sequence(7))
        