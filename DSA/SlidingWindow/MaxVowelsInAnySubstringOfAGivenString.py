class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(char: str) -> bool:
            return char in ['a', 'e', 'i', 'o', 'u']
        
        n = len(s)
        max_vowels, vowels = 0, 0
        for i in range(k):
            if isVowel(s[i]):
                vowels += 1
        max_vowels = vowels

        for i in range(k, n):
            if isVowel(s[i]):
                vowels += 1
            if isVowel(s[i-k]):
                vowels -= 1
            max_vowels = max(max_vowels, vowels)
        
        return max_vowels
