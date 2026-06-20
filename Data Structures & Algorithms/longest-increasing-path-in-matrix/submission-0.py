class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        memo = {}
        m,n = len(grid), len(grid[0])
        def solve(i,j):
            if (i,j) in memo: return memo[(i,j)]
            best = 1
            for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    best = max(best, solve(ni,nj)+1)
            memo[(i,j)] = best
            return memo[(i,j)]
        for i in range(m):
            for j in range(n):
                solve(i,j)
        return max(memo.values())