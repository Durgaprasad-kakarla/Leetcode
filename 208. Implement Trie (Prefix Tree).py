class TrieNode:
    def __init__(self):
        self.links=[None]*26
        self.flag=False
    def contain_key(self,ch):
        return self.links[ord(ch)-ord('a')] is not None
    def put(self,ch,node):
        self.links[ord(ch)-ord('a')]=node
    def get(self,ch):
        return self.links[ord(ch)-ord('a')]
    def set_end(self):
        self.flag=True
    def is_end(self):
        return self.flag


class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        node=self.root
        for char in word:
            if not node.contain_key(char):
                node.put(char,TrieNode())
            node=node.get(char)
        node.set_end()

    def search(self, word: str) -> bool:
        node=self.root
        for char in word:
            if not node.contain_key(char):
                return False
            node=node.get(char)
        return node.is_end()

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for char in prefix:
            if not node.contain_key(char):
                return False
            node=node.get(char)
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
''' Time Complexity--O(n)
    Space Complexity--O(1)'''
