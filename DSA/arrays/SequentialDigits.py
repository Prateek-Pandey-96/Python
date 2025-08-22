class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        for i in range(1, 10):
            num = 0
            for j in range(i, 10):
                num = num*10 + j
                if num >= low and num <= high:
                    result.append(num)
        return sorted(result)
