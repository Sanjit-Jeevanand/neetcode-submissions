class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid), len(grid[0])
        dq = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dq.append((i,j))
        x = 0
        while dq:
            x += 1
            lvl = len(dq)
            for _ in range(lvl):
                i,j = dq.popleft()
                for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 2147483647:
                        grid[ni][nj] = x
                        dq.append((ni,nj))