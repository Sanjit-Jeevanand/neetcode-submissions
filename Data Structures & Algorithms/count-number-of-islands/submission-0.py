class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        ans = 0
        def dfs(i,j):
            grid[i][j] = "0"
            for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == "1":
                    dfs(ni,nj)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i,j)
        return ans