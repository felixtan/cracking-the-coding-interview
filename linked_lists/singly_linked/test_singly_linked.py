import unittest
from singly_linked import Node, LinkedList

class TestSinglyLinkedList(unittest.TestCase):
    def test_init_list(self):
        head = Node('foo')
        ll = LinkedList(head)
        self.assertEqual(ll.head, head)
        self.assertEqual(ll.tail, head)
        self.assertEqual(ll.head.next, None)
        self.assertEqual(ll.__repr__(), '[<singly_linked.Node foo>]')

    def test_appends_node(self):
        head = Node('foo')
        ll = LinkedList(head)
        ll.append('bar')
        self.assertEqual(ll.head.value, 'foo')
        self.assertEqual(ll.head.next.value, 'bar')
        self.assertEqual(ll.tail.value, 'bar')

    def test_prepends_node(self):
        head = Node('foo')
        ll = LinkedList(head)
        ll.prepend('bar')
        self.assertEqual(ll.head.value, 'bar')
        self.assertEqual(ll.head.next.value, 'foo')
        self.assertEqual(ll.tail.value, 'foo')

    def test_delete_node(self):
        head = Node('foo')
        ll = LinkedList(head)
        ll.append('bar')
        ll.append('baz')
        
        head = ll.delete('baz')
        self.assertEqual(head.value, 'foo')
        self.assertEqual(ll.head.value, 'foo')
        self.assertEqual(ll.head.next.value, 'bar')
        self.assertEqual(ll.tail.value, 'bar')
        
        head = ll.delete('foo')
        self.assertEqual(head.value, 'bar')
        self.assertEqual(ll.head.value, 'bar')
        self.assertEqual(ll.tail.value, 'bar')