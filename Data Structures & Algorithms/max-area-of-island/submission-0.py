class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        ans = 0
        def dfs(i,j,x):
            grid[i][j] = 0
            count = 0
            for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    count += dfs(ni,nj,1)
            return x+count
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x = dfs(i,j,1)
                    ans = max(ans,x)
        return ans