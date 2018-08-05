import unittest
import heap
from tree import Node

class MinHeapTest(unittest.TestCase):
    def test_is_min_heap(self):
        root = Node(0)
        root.left = Node(1)
        root.right = Node(2)
        root.left.left = Node(3)
        self.assertTrue(isinstance(heap.MinHeap(root), heap.MinHeap))

        root.left.value = 4
        self.assertRaises(Exception, heap.MinHeap, root)      # not ordered

        root.left.value = 1
        root.right.left = Node(5)
        self.assertRaises(Exception, heap.MinHeap, root)      # not complete

        root.left.right = Node(6)
        self.assertTrue(isinstance(heap.MinHeap(root), heap.MinHeap))

    def test_insert(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        min_heap = heap.MinHeap(root)

        min_heap.insert(0)
        self.assertTrue(min_heap.is_min_heap)
        self.assertEqual(min_heap.root.value, 0)
        self.assertEqual(min_heap.root.left, 1)
        self.assertEqual(min_heap.root.right, 3)
        self.assertEqual(min_heap.root.left.left, 4)
        self.assertEqual(min_heap.root.left.left, 2)

    def test_extract_min(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        min_heap = heap.MinHeap(root)

        min = min_heap.extract_min()
        self.assertEqual(min, 1)
        self.assertEqual(min_heap.is_min_heap)
        self.assertEqual(min_heap.root.value, 2)
        self.assertEqual(min_heap.root.left.value, 4)
        self.assertEqual(min_heap.root.right.value, 3)
        self.assertEqual(min_heap.root.left.left.value, 5)
