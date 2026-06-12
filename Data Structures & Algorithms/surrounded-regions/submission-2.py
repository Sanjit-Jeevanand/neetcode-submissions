class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        m,n = len(grid), len(grid[0])
        dq = deque()
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m-1 or j == n-1) and grid[i][j] == "O":
                    grid[i][j] = "#"
                    dq.append((i,j))
        while dq:
            i,j = dq.popleft()
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "O":
                    grid[ni][nj] = "#"
                    dq.append((ni,nj))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "O":
                    grid[i][j] = "X"
                if grid[i][j] == "#":
                    grid[i][j] = "O"