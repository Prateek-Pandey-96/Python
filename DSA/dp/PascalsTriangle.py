class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        removal = 0
        for i in range(1, numRows):
            size = len(result[-1])*2 - removal
            removal += 1
            temp = [1]*size
            for j in range(1, size-1):
                temp[j] = result[-1][j] + result[-1][j-1]
            result.append(temp)
        
        return result
