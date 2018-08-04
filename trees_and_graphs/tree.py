class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    @property
    def height(self):
        def _height(node):
            if node and (node.left or node.right):
                return 1 + max(_height(node.left), _height(node.right))
            else:
                return 0
        return _height(self)

class Tree:
    def __init__(self, root):
        self.root = root

class BinaryTree(Tree):
    def __init__(self, root):
        super().__init__(root)

    def traverse_inorder(self, fn):
        def _traverse(node):
            if node:
                _traverse(node.left)
                fn(node)
                _traverse(node.right)
        _traverse(self.root)

    def traverse_preorder(self, fn):
        def _traverse(node):
            if node:
                fn(node)
                _traverse(node.left)
                _traverse(node.right)
        _traverse(self.root)

    def traverse_postorder(self, fn):
        def _traverse(node):
            if node:
                _traverse(node.left)
                _traverse(node.right)
                fn(node)
        _traverse(self.root)

    @property
    def height(self):
      return self.root.height

    @property
    def is_balanced(self):
        return abs(self.root.left.height - self.root.right.height) <= 1

    @property
    def is_complete(self):
        def check_complete(node):
            if node and node.right:
                return node.left and check_complete(node.left) and check_complete(node.right)
            else:
                return True
        return check_complete(self.root)

    @property
    def is_full(self):
        def check_full(node):
            if not node:
                return True
            else:
                if bool(node.left) != bool(node.right):
                    return False
                else:
                    return check_full(node.left) and check_full(node.right)
        return check_full(self.root)

    @property
    def is_min_heap(self):
        def is_ordered(node):
            if node:
                if ((node.left and node.value < node.left.value) or not node.left) and ((node.right and node.value < node.right.value) or not node.right):
                    return True and is_ordered(node.left) and is_ordered(node.right)
                else:
                    return False
            else:
                return True
        print(is_ordered(self.root))
        print(self.is_complete)
        return self.is_complete and is_ordered(self.root)
