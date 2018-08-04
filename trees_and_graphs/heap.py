import tree

class MinHeap(tree.BinaryTree):
    def __init__(self, root):
        if isinstance(root, tree.BinaryTree):
            if btree.is_min_heap:
                super().__init__(root)
            else:
                raise ValueError('Given tree is not a valid min heap')
        elif isinstance(root, tree.Node):
            btree = tree.BinaryTree(root)
            if btree.is_min_heap:
                super().__init__(root)
            else:
                raise ValueError('Given root is not part of a valid min heap')
        else:
            raise TypeError('MinHeap must be initialized with a Node or BinaryTree')

    # @property
    # def is_min_hea
