import unittest
from robot.robot import traverse

class TestRobot(unittest.TestCase):
    def test_exits(self):
        grid = [
            ['o','o','o','o'],
            ['x','x','x','o'],
            ['o','o','o','o'],
            ['o','o','o','o'],
        ]
        paths = traverse(grid)
        self.assertIn([(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3)], paths)

    def test_return_none_if_no_path(self):
        grid = [
            ['o','o','o','o'],
            ['x','x','x','x'],
            ['o','o','o','o'],
            ['o','o','o','o'],
        ]
        paths = traverse(grid)
        self.assertEqual(paths, [])

if __name__ == '__main__':
    unittest.main()
