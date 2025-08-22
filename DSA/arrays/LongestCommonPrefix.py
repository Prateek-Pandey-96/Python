class Solution:
    def numDigits(self, num):
        digits = 0
        while num>0:
            num = num//10
            digits += 1
        return digits

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        elements = set()
        for num in arr1:
            while num > 0:
                elements.add(num)
                num //= 10
        
        longest = 0
        for num in arr2:
            while num > 0:
                digits = self.numDigits(num)
                if num in elements:
                    longest = max(longest, digits)
                num //= 10
        
        return longest
