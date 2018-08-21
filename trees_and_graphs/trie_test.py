import unittest
import trie

class TestTrie(unittest.TestCase):
    def test_gets_words(self):
        t = trie.Trie(['door', 'deer', 'dear'])
        words = t.get_words('de')
        self.assertIn('deer', words)
        self.assertIn('dear', words)
        self.assertNotIn('door', words)

if __name__ == '__main__':
    unittest.main()
