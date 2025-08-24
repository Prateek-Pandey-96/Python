class Solution:
    def tokenize(self, sentence) -> List[str]:
        temp = []
        tokens = []
        for ch in sentence:
            if ch == ' ':
                tokens.append(''.join(temp))
                temp = []
            else:
                temp.append(ch)
        if len(temp):
            tokens.append(''.join(temp))
        return tokens
    
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        tokens1, tokens2 = self.tokenize(sentence1), self.tokenize(sentence2)
        m, n = len(tokens1), len(tokens2)
        if m < n:
            return self.areSentencesSimilar(sentence2, sentence1)
        lcp, lcs = 0, 0
        i, j = 0, 0
        while i < m and j< n and tokens1[i]==tokens2[j]:
            i += 1
            j += 1
            lcp += 1
        
        i, j = m-1, n-1
        while i>=0 and j >=0 and tokens1[i]==tokens2[j]:
            i -= 1
            j -= 1
            lcs += 1
        return lcp + lcs >= n
        

        
        


