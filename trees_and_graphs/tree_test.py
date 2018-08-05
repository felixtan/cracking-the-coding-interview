import unittest
import tree
from tree import Node

def store_ordering(order_list):
    def _store_ordering(node):
        order_list.append(node.value)
    return _store_ordering

class BinaryTreeTest(unittest.TestCase):
    def test_check_balanced(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.right.left = Node(3)
        root.right.right = Node(4)
        root.right.right.left = Node(5)
        btree = tree.BinaryTree(root)
        self.assertFalse(btree.is_balanced)

        root.left.left = Node(6)
        self.assertTrue(btree.is_balanced)

    def test_check_full(self):
        root = Node(0)
        btree = tree.BinaryTree(root)
        self.assertTrue(btree.is_full)

        root.left = Node(1)
        self.assertFalse(btree.is_full)

        root.right = Node(2)
        self.assertTrue(btree.is_full)

    def test_inorder_traversal(self):
        ordering = []
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(3)
        root.right.left = Node(4)
        root.right.right = Node(5)
        btree = tree.BinaryTree(root)
        btree.traverse_inorder(store_ordering(ordering))
        self.assertEqual(ordering, [3, 1, 0, 4, 2, 5])

    def test_preorder_traversal(self):
        ordering = []
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(3)
        root.right.left = Node(4)
        root.right.right = Node(5)
        btree = tree.BinaryTree(root)
        btree.traverse_preorder(store_ordering(ordering))
        self.assertEqual(ordering, [0, 1, 3, 2, 4, 5])

    def test_postorder_traversal(self):
        ordering = []
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(3)
        root.right.left = Node(4)
        root.right.right = Node(5)
        btree = tree.BinaryTree(root)
        btree.traverse_postorder(store_ordering(ordering))
        self.assertEqual(ordering, [3, 1, 4, 5, 2, 0])

    def test_calc_height(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(3)
        root.right.left = Node(4)
        root.right.right = Node(5)
        btree = tree.BinaryTree(root)
        self.assertEqual(btree.height, 2)

        root.right.right.right = Node(6)
        self.assertEqual(btree.height, 3)

    def test_check_complete_confirm(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        btree = tree.BinaryTree(root)
        self.assertTrue(btree.is_complete)

        root.left.left = Node(3)
        self.assertTrue(btree.is_complete)

        root.left.right = Node(4)
        self.assertTrue(btree.is_complete)

    def test_check_complete_falsify(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.right.left = Node(3)
        btree = tree.BinaryTree(root)
        self.assertFalse(btree.is_complete)

        # subtrees are complete
        root.left.left = Node(4)
        self.assertFalse(btree.is_complete)
        root.right.right = Node(5)
        self.assertFalse(btree.is_complete)

        root.left.left = None
        root.right.right = None

        # left and right subtrees have the same number of nodes
        root.left.right = Node(4)
        self.assertFalse(btree.is_complete)

        root.right.left = None
        self.assertFalse(btree.is_complete)

        # left and right subtrees are of equal height
        root.left.left = Node(3)
        root.right.right = Node(5)
        self.assertFalse(btree.is_complete)

        # left subtree is taller than right by more than 1
        root.right.right = None
        root.left.left.left = Node(6)
        root.left.left.right = Node(7)
        self.assertFalse(btree.is_complete)

    def test_check_perfect(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        btree = tree.BinaryTree(root)
        self.assertTrue(btree.is_perfect)

        root.left.left = Node(3)
        self.assertFalse(btree.is_perfect)

        root.left.right = Node(4)
        self.assertTrue(btree.is_perfect)

        root.right.left = Node(5)
        self.assertFalse(btree.is_perfect)

        root.right.right = Node(6)
        self.assertTrue(btree.is_perfect)

        temp = root.right
        root.right = None
        self.assertFalse(btree.is_perfect)

        root.right = temp
        temp = root.left
        root.left = None
        self.assertFalse(btree.is_perfect)

    def test_count_nodes(self):
        btree = tree.BinaryTree()
        self.assertEqual(btree.nodes, 0)

        root = Node(0)
        btree.root = root
        self.assertEqual(btree.nodes, 1)

        root.left = Node(1)
        self.assertEqual(btree.nodes, 2)

        root.right = Node(2)
        self.assertEqual(btree.nodes, 3)

        root.right.right = Node(3)
        self.assertEqual(btree.nodes, 4)

        root.right.left = Node(4)
        self.assertEqual(btree.nodes, 5)

if __name__ == '__main__':
  unittest.main()
