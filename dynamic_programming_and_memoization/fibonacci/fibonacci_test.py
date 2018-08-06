import unittest
from recursive import fibonacci as recursive_not_memoized
from recursive_memoized import fibonacci as recursive_memoized
from iterative import fibonacci as iterative

class TestFibonacci(unittest.TestCase):
    def test_recursive_not_memoized(self):
        self.assertRaises(ValueError, recursive_not_memoized, -1)
        self.assertEqual(recursive_not_memoized(0), 0)
        self.assertEqual(recursive_not_memoized(1), 1)
        self.assertEqual(recursive_not_memoized(2), 1)
        self.assertEqual(recursive_not_memoized(3), 2)
        self.assertEqual(recursive_not_memoized(4), 3)
        self.assertEqual(recursive_not_memoized(5), 5)
        self.assertEqual(recursive_not_memoized(6), 8)
        self.assertEqual(recursive_not_memoized(7), 13)
        self.assertEqual(recursive_not_memoized(8), 21)
        self.assertEqual(recursive_not_memoized(9), 34)

    def test_recursive_memoized(self):
        self.assertRaises(ValueError, recursive_memoized, -1)
        self.assertEqual(recursive_memoized(0), 0)
        self.assertEqual(recursive_memoized(1), 1)
        self.assertEqual(recursive_memoized(2), 1)
        self.assertEqual(recursive_memoized(3), 2)
        self.assertEqual(recursive_memoized(4), 3)
        self.assertEqual(recursive_memoized(5), 5)
        self.assertEqual(recursive_memoized(6), 8)
        self.assertEqual(recursive_memoized(7), 13)
        self.assertEqual(recursive_memoized(8), 21)
        self.assertEqual(recursive_memoized(9), 34)

    def test_iterative(self):
        self.assertRaises(ValueError, iterative, -1)
        self.assertEqual(iterative(0), 0)
        self.assertEqual(iterative(1), 1)
        self.assertEqual(iterative(2), 1)
        self.assertEqual(iterative(3), 2)
        self.assertEqual(iterative(4), 3)
        self.assertEqual(iterative(5), 5)
        self.assertEqual(iterative(6), 8)
        self.assertEqual(iterative(7), 13)
        self.assertEqual(iterative(8), 21)
        self.assertEqual(iterative(9), 34)
