class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result
        
        if k > 0:
            result[0] = 0
            for i in range(1, k+1):
                result[0] += code[i]
            for i in range(1, n):
                result[i] = result[i-1] - code[i] + code[(i+k)%n]
        
        if k < 0:
            k = -k
            code.reverse()
            result[0] = 0
            for i in range(1, k+1):
                result[0] += code[i]
            for i in range(1, n):
                result[i] = result[i-1] - code[i] + code[(i+k)%n]
            result.reverse()
        return result



