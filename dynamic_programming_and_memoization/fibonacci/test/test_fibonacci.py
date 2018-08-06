import unittest
from fibonacci.recursive import fibonacci as recursive_not_memoized
from fibonacci.recursive_memoized import fibonacci as recursive_memoized
from fibonacci.iterative import fibonacci as iterative

F = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

class TestFibonacci(unittest.TestCase):
    def test_recursive_not_memoized(self):
        self.assertRaises(ValueError, recursive_not_memoized, -1)
        for i in range(10):
            self.assertEqual(recursive_not_memoized(i), F[i])

    def test_recursive_memoized(self):
        self.assertRaises(ValueError, recursive_memoized, -1)
        for i in range(10):
            self.assertEqual(recursive_memoized(i), F[i])

    def test_iterative(self):
        self.assertRaises(ValueError, iterative, -1)
        for i in range(10):
            self.assertEqual(iterative(i), F[i])

if __name__ == '__main__':
  unittest.main()
