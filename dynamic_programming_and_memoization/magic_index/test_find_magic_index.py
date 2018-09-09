import unittest
import random
from magic_index import binary_search

class TestFindMagicIndex(unittest.TestCase):
    def test_distinct_search(self):
        arr1 = [0, 3, 5, 6, 7, 8, 10, 11, 13, 15]
        self.assertEqual(binary_search(arr1), 0)

        arr2 = [1, 3, 4, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(binary_search(arr2), None)

        arr3 = [-3, -1, 0, 3, 8, 9, 10, 11, 12, 13]
        self.assertEqual(binary_search(arr3), 3)

        arr4 = [-2, -1, 0, 1, 2, 3, 4, 5, 8]
        self.assertEqual(binary_search(arr4), 8)

    def test_nondistinct_search(self):
        arr1 = [1, 1, 4, 7, 8, 9, 10, 11, 12, 13]
        self.assertEqual(binary_search(arr1), 1)

        arr2 = [1, 2, 4, 4, 8, 9, 10, 11, 12, 13]
        self.assertEqual(binary_search(arr2), None)

        arr3 = [-3, -1, -1, 3, 8, 9, 10, 11, 11, 13]
        self.assertEqual(binary_search(arr3), 3)

        arr4 = [-3, -1, -1, 2, 3, 3, 6, 11, 11, 13]
        self.assertEqual(binary_search(arr4), 6)

        arr5 = [-1, -1, -1, -1, -1, -1, -1, -1, 8]
        self.assertEqual(binary_search(arr5), 8)