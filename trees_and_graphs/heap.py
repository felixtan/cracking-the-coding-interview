import tree

class MinHeap(tree.BinaryTree):
    def __init__(self, root):
        if isinstance(root, tree.BinaryTree):
            if btree.is_min_heap:
                super().__init__(root)
            else:
                raise ValueError('Given tree is not a min heap')
        elif isinstance(root, tree.Node):
            btree = tree.BinaryTree(root)
            if btree.is_min_heap:
                super().__init__(root)
            else:
                raise ValueError('Given root node is not part of a min heap')
        else:
            raise TypeError('MinHeap must be initialized with a Node or BinaryTree')

    def insert(self, value):
        node = value if isinstance(value, tree.Node) else tree.Node(value)
        pass

    def extract_min(self):
        pass
