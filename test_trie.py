import unittest
from trie import Trie

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))  # app is prefix but not inserted yet

    def test_starts_with(self):
        self.trie.insert("app")
        self.assertTrue(self.trie.starts_with("ap"))
        self.assertFalse(self.trie.starts_with("ba"))

    def test_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))

    def test_multiple_words(self):
        words = ["cat", "cap", "can"]
        for word in words:
            self.trie.insert(word)
        for word in words:
            self.assertTrue(self.trie.search(word))
        self.assertFalse(self.trie.search("cab"))

if __name__ == '__main__':
    unittest.main()
