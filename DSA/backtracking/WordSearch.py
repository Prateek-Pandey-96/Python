class Solution:
    def find(self, idx, x, y, word, board) -> bool:
        if idx == len(word)-1:
            return board[x][y]==word[idx]
        temp = board[x][y]
        board[x][y] = '#'
        for i in range(4):
            newx, newy = x + self.dx[i], y + self.dy[i]
            if newx < 0 or newy < 0 or newx >= self.m or newy >= self.n:
                continue
            if word[idx+1] == board[newx][newy]:
                found = self.find(idx+1, newx, newy, word, board)
                if found:
                    return True
        board[x][y] = temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m, self.n = len(board), len(board[0])
        self.dx, self.dy = [1, -1, 0, 0], [0, 0, 1, -1]
        
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    if self.find(0, i, j, word, board):
                        return True
        
        return False
