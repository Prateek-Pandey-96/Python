class TrieNode:
    def __init__(self, data):
        self.data: str = data
        self.children = [None] * 26
        self.ends: bool = False

class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode("")

    def addWord(self, word: str) -> None:
        crawler = self.root
        for ch in word:
            idx = ord(ch)-ord('a')
            if crawler.children[idx] is None:
                crawler.children[idx] = TrieNode("")
            crawler.children[idx].data = ch
            crawler = crawler.children[idx]
        crawler.ends = True

    def helper(self, idx, word, crawler) -> bool:
        if idx == len(word):
            return crawler.ends
        
        i = ord(word[idx]) - ord('a')
        # if actual char is present
        if word[idx] != '.':
            if crawler.children[i] is None or crawler.children[i].data != word[idx]:
                return False
            return self.helper(idx+1, word, crawler.children[i])
        
        # if dot is present check with each children
        for it in range(26):
            if crawler.children[it] is None:
                continue
            if self.helper(idx+1, word, crawler.children[it]):
                return True
        return False
    
    def search(self, word: str) -> bool:
        crawler = self.root
        return self.helper(0, word, crawler)
