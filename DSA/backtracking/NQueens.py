class Solution:
    def isSafe(self, i: int, j: int, solution: List[List[chr]]):
        n = len(solution)
        
        for col in range(n):
            if solution[i][col] == 'Q':
                return False
        
        for row in range(n):
            if solution[row][j] == 'Q':
                return False
    
        row, col = i, j
        while row>=0 and col<n:
            if solution[row][col] == 'Q':
                return False
            row -= 1
            col += 1
        
        row, col = i, j
        while row>=0 and col>=0:
            if solution[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
    
        return True

    def helper(self, idx: int, n: int, solution: List[List[chr]], result: List[List[str]]) -> None:
        if idx >= n:
            temp = []
            for row in solution:
                temp.append(''.join(row))
            result.append(temp)
            return
        
        for j in range(n):
            if self.isSafe(idx, j, solution):
                solution[idx][j] = 'Q'
                self.helper(idx+1, n, solution, result)
                solution[idx][j] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        solution = [['.' for _ in range(n)] for _ in range(n)]
        self.helper(0, n, solution, result)
        return result
