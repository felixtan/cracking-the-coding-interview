import unittest
import tree

def store_ordering(order_list):
    def _store_ordering(node):
        order_list.append(node.value)
    return _store_ordering

class BinaryTreeTest(unittest.TestCase):
    def test_check_balanced(self):
        root = tree.Node('a')
        root.left = tree.Node('b')
        root.right = tree.Node('c')
        root.right.left = tree.Node('d')
        root.right.right = tree.Node('e')
        root.right.right.left = tree.Node('f')
        btree = tree.BinaryTree(root)
        self.assertFalse(btree.is_balanced)

        root.left.left = tree.Node('g')
        self.assertTrue(btree.is_balanced)

    def test_check_complete(self):
        root = tree.Node('a')
        root.left = tree.Node('b')
        root.right = tree.Node('c')
        root.left.left = tree.Node('d')
        root.left.right = tree.Node('e')
        root.right.right = tree.Node('f')
        btree = tree.BinaryTree(root)
        self.assertFalse(btree.is_complete)

        root.right.left = tree.Node('g')
        self.assertTrue(btree.is_complete)

    def test_check_full(self):
        root = tree.Node('a')
        btree = tree.BinaryTree(root)
        self.assertTrue(btree.is_full)

        root.left = tree.Node('b')
        self.assertFalse(btree.is_full)

        root.right = tree.Node('c')
        self.assertTrue(btree.is_full)

    def test_inorder_traversal(self):
        ordering = []
        root = tree.Node(0)
        root.left = tree.Node(1)
        root.right = tree.Node(2)
        root.left.left = tree.Node(3)
        root.right.left = tree.Node(4)
        root.right.right = tree.Node(5)
        btree = tree.BinaryTree(root)
        btree.traverse_inorder(store_ordering(ordering))
        self.assertEqual(ordering, [3, 1, 0, 4, 2, 5])

    def test_preorder_traversal(self):
        ordering = []
        root = tree.Node(0)
        root.left = tree.Node(1)
        root.right = tree.Node(2)
        root.left.left = tree.Node(3)
        root.right.left = tree.Node(4)
        root.right.right = tree.Node(5)
        btree = tree.BinaryTree(root)
        btree.traverse_preorder(store_ordering(ordering))
        self.assertEqual(ordering, [0, 1, 3, 2, 4, 5])

    def test_postorder_traversal(self):
        ordering = []
        root = tree.Node(0)
        root.left = tree.Node(1)
        root.right = tree.Node(2)
        root.left.left = tree.Node(3)
        root.right.left = tree.Node(4)
        root.right.right = tree.Node(5)
        btree = tree.BinaryTree(root)
        btree.traverse_postorder(store_ordering(ordering))
        self.assertEqual(ordering, [3, 1, 4, 5, 2, 0])

    def test_calc_height(self):
        root = tree.Node(0)
        root.left = tree.Node(1)
        root.right = tree.Node(2)
        root.left.left = tree.Node(3)
        root.right.left = tree.Node(4)
        root.right.right = tree.Node(5)
        btree = tree.BinaryTree(root)
        self.assertEqual(btree.height, 2)

        root.right.right.right = tree.Node(6)
        self.assertEqual(btree.height, 3)

    def test_complete_v2(self):
        root = tree.Node(0)
        root.left = tree.Node(1)
        root.right = tree.Node(2)
        root.left.left = tree.Node(3)
        root.right.left = tree.Node(5)
        btree = tree.BinaryTree(root)
        self.assertFalse(btree.is_complete)

if __name__ == '__main__':
  unittest.main()
