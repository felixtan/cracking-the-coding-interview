import unittest
from mergesort import mergesort

class TestMergesort(unittest.TestCase):
    def test_sorts(self):
        arr = [38, 27, 43, 3, 9, 82, 10]
        self.assertEqual(mergesort(arr), sorted(arr))

    def test_sort_negative(self):
        arr = [38, 27, 43, -3, 9, -82, 10]
        self.assertEqual(mergesort(arr), sorted(arr))