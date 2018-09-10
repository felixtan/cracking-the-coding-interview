import unittest
from power_set import generate_subsets

class TestGeneratePowerSet(unittest.TestCase):
    def test_generate_subsets(self):
        my_set = {0, 1, 2}
        power_set = generate_subsets(my_set)
        expected = (set(), {0}, {1}, {2}, {0, 1}, {0, 2}, {1, 2}, {0, 1, 2})
        for s in expected:
            self.assertIn(s, power_set)