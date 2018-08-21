class Node:
    def __init__(self, value):
        self.value = value
        self.children = {}


class Trie:
    def __init__(self, words):
        """Initialize trie with a list of words
        """
        self.root = Node('')

        for word in words:
            self.insert_word(word)

    # O(len(word))
    def insert_word(self, word, node = None):
        if not node:
            node = self.root

        if word:
            char = word[0]

            if char in node.children:
                child = node.children[char]
            else:
                child = Node(char)
                node.children[char] = child

            self.insert_word(word[1:], child)


    # O(len(prefix))
    def find_prefix_node(self, prefix, node = None):
        if not node:
            node = self.root

        if not prefix:
            return node
        else:
            char = prefix[0]

            if char in node.children:
                return self.find_prefix_node(prefix[1:], node.children[char])
            else:
                return None

    def get_words(self, prefix, node = None):
        if not node:
            node = self.root

        prefix_node = self.find_prefix_node(prefix)
        words = []

        if prefix_node:
            def traverse(word, node):
                if not node.children:
                    words.append(word)
                else:
                    for child in node.children.values():
                        traverse(word + child.value, child)

            traverse(prefix, prefix_node)

        return words
