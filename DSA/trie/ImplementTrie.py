class TrieNode:
    def __init__(self, data):
        self.data: str = data
        self.children: List[TrieNode] = [None] * 26
        self.ends: bool = False

class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        crawler = self.root
        for ch in word:
            idx = ord(ch)-ord('a')
            if crawler.children[idx] is None:
                crawler.children[idx] = TrieNode("")
            crawler.children[idx].data = ch
            crawler = crawler.children[idx]
        crawler.ends = True

    def search(self, word: str) -> bool:
        crawler = self.root
        for ch in word:
            idx = ord(ch)-ord('a')
            if crawler.children[idx] is None:
                return False
            crawler = crawler.children[idx]
        return crawler.ends == True

    def startsWith(self, prefix: str) -> bool:
        crawler = self.root
        for ch in prefix:
            idx = ord(ch)-ord('a')
            if crawler.children[idx] is None:
                return False
            crawler = crawler.children[idx]
        return True



