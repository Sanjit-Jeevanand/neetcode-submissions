class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):
            s1 = set()
            s2 = set()
            for j in range(n):
                if board[i][j] in s1:
                    return False
                elif board[i][j] != ".":
                    s1.add(board[i][j])
                if board[j][i] in s2:
                    return False
                elif board[j][i] != ".":
                    s2.add(board[j][i])
        for i,j in [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]:
            s = set()
            for x in range(i,i+3):
                for y in range(j,j+3):
                    if board[x][y] in s:
                        return False
                    elif board[x][y] != ".":
                        s.add(board[x][y])
        return True