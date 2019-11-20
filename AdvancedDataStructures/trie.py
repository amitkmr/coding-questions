import unittest


class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_leaf = False


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, key):
        current_node = self.root
        for char in key:
            if not current_node.children[self._get_char_index(char)]:
                current_node.children[self._get_char_index(char)] = TreeNode()
            current_node = current_node.children[self._get_char_index(char)]

        current_node.is_leaf = True

    def search(self, key):
        current_node = self.root
        for char in key:
            if not current_node.children[self._get_char_index(char)]:
                return False
            else:
                current_node = current_node.children[self._get_char_index(char)]

        if current_node.is_leaf:
            return True
        else:
            return False

    def _get_char_index(self, char):
        return ord(char) - ord("a")


class TestCase(unittest.TestCase):
    def test_sample(self):
        keys = ["the", "a", "there", "anaswe", "any", "by", "their"]

        trie = Trie()
        for key in keys:
            trie.insert(key)

        search_keys = ["the", "a", "there", "anaswe", "any", "by", "amk"]
        for key in search_keys:
            if trie.search(key):
                print("Present!")
            else:
                print("Absent!")


if __name__ == "__main__":
    unittest.main()
