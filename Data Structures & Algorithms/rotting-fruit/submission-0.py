class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        fresh = 0
        dq = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    dq.append((i,j))
        t = 0
        while dq and fresh > 0:
            t += 1
            lvl = len(dq)
            for _ in range(lvl):
                i,j = dq.popleft()
                for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        fresh -= 1
                        grid[ni][nj] = 2
                        dq.append((ni,nj))
        return t if fresh == 0 else -1
        