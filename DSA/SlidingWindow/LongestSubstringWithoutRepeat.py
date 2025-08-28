class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i, j = 0, 0
        freq = defaultdict(int)
        max_len = 0
        while j<n:
            freq[s[j]] += 1

            while i<=j and freq[s[j]]>1:
                freq[s[i]] -= 1
                i += 1
            
            max_len = max(max_len, j-i+1)
            j += 1
        return max_len


