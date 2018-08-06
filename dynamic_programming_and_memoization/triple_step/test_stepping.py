import unittest
from stepping import generate_ways

class TestStepping(unittest.TestCase):
    def test_generates_ways(self):
        self.assertRaises(ValueError, generate_ways, 0)
        self.assertRaises(ValueError, generate_ways, -1)

        ways = generate_ways(5)
        self.assertEqual(len(ways), 13)
        self.assertIn([1, 1, 1, 1, 1], ways)
        self.assertIn([1, 1, 1, 2], ways)
        self.assertIn([1, 1, 3], ways)
        self.assertIn([1, 1, 2, 1], ways)
        self.assertIn([1, 2, 1, 1], ways)
        self.assertIn([1, 2, 2], ways)
        self.assertIn([1, 3, 1], ways)
        self.assertIn([2, 1, 1, 1], ways)
        self.assertIn([2, 1, 2], ways)
        self.assertIn([2, 2, 1], ways)
        self.assertIn([2, 3], ways)
        self.assertIn([3, 1, 1], ways)
        self.assertIn([3, 2], ways)

if __name__ == '__main__':
    unittest.main()
