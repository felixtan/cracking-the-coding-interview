class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    @property
    def height(self):
        def calc_height(node):
            if node and (node.left or node.right):
                return 1 + max(calc_height(node.left), calc_height(node.right))
            else:
                return 0
        return calc_height(self)

class Tree:
    def __init__(self, root = None):
        self.root = root

class BinaryTree(Tree):
    def __init__(self, root = None):
        super().__init__(root)

    def traverse_inorder(self, fn):
        def traverse(node):
            if node:
                traverse(node.left)
                fn(node)
                traverse(node.right)
        traverse(self.root)

    def traverse_preorder(self, fn):
        def traverse(node):
            if node:
                fn(node)
                traverse(node.left)
                traverse(node.right)
        traverse(self.root)

    def traverse_postorder(self, fn):
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                fn(node)
        traverse(self.root)

    @property
    def height(self):
        return self.root.height

    @property
    def left(self):
        return BinaryTree(self.root.left) if self.root.left else None

    @property
    def right(self):
        return BinaryTree(self.root.right) if self.root.right else None

    @property
    def nodes(self):
        class Counter:
            def __init__(self):
                self.value = 0

            def incr(self):
                self.value += 1

        def count_nodes(counter):
            def _count_nodes(node):
                if node: counter.incr()
            return _count_nodes

        counter = Counter()
        self.traverse_preorder(count_nodes(counter))

        return counter.value

    @property
    def is_balanced(self):
        return abs(self.left.height - self.right.height) <= 1

    @property
    def is_complete(self):
        def children_are_ordered(reducer):
            def _children_are_ordered(node):
                reducer.value = reducer.value and (node.right and node.left or not node.right)
            return _children_are_ordered

        def subtrees_are_ordered(tree):
            class BoolReducer:
                def __init__(self, value = None):
                    self.value = bool(value)

            reducer = BoolReducer(True)
            self.traverse_preorder(children_are_ordered(reducer))
            return reducer.value

        def left_is_filled_first(tree):
            left, right = BinaryTree(tree.left), BinaryTree(tree.right)
            return left.nodes >= right.nodes if tree.is_full else left.nodes > right.nodes

        return (subtrees_are_ordered(self) and
                left_is_filled_first(self) and
                self.left.height - self.right.height in [0, 1])

    @property
    def is_full(self):
        def check_full(tree):
            if not tree:
                return True
            else:
                if bool(tree.left) != bool(tree.right):
                    return False
                else:
                    return check_full(tree.left) and check_full(tree.right)
        return check_full(self)

    @property
    def is_perfect(self):
        return self.is_full and self.is_complete

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

        return self.is_complete and is_ordered(self.root)
