import unittest
from recursive_multiply import multiply

class TestRecursiveMultipy(unittest.TestCase):
    def test_mult_by_zero(self):
        self.assertEqual(multiply(3, 0), 0)

    def test_mult_by_one(self):
        self.assertEqual(multiply(3, 1), 3)

    def test_mult_one_negative(self):
        self.assertEqual(multiply(3, -2), -6)

    def test_mult_two_negative(self):
        self.assertEqual(multiply(-3, -2), 6)