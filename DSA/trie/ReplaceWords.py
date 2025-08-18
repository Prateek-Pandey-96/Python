class TrieNode:
    def __init__(self, data):
        self.data: str = data
        self.children = [None] * 26
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

    def findRootWord(self, word: str) -> str:
        crawler = self.root
        curr = []
        for ch in word:
            idx = ord(ch)-ord('a')
            curr.append(ch)
            if crawler.children[idx] is None:
                break
            crawler = crawler.children[idx]
            if crawler.ends == True:
                return "".join(curr)
            
        if crawler.ends == True:
            return "".join(curr)
            
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for word in dictionary:
            trie.insert(word)
        
        result = []
        temp = []
        for ch in sentence:
            if ch == " ":
                result.append(trie.findRootWord("".join(temp)))
                temp = []
            else:
                temp.append(ch)
        if temp != []:
            result.append(trie.findRootWord("".join(temp)))
        return " ".join(result)
