"""
This question was really cool:

Implement a trie (prefix tree) data structure that supports insertion, search, and deletion of strings.
Additionally, implement a method to find all strings in the trie that start with a given prefix.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def delete(self, word):
        def _delete(node, word, index):
            if index == len(word):
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[index]
            if char not in node.children:
                return False

            child_node = node.children[char]
            should_delete_child = _delete(child_node, word, index + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0

            return False

        _delete(self.root, word, 0)

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        words = []
        self._collect_words(node, prefix, words)
        return words

    def _collect_words(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)

        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, words)
            
trie = Trie()

trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("applet")

print(trie.search("apple")) # Output: True
print(trie.search("app")) # Output: True
print(trie.search("banana")) # Output: True
print(trie.search("grape")) # Output: False

print(trie.starts_with("app")) # Output: ['app', 'apple', 'applet']
print(trie.starts_with("ban")) # Output: ['banana']
print(trie.starts_with("gr")) # Output: []

trie.delete("apple")
print(trie.search("apple")) # Output: False
print(trie.starts_with("app")) # Output: ['app', 'applet']