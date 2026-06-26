class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        dq1, dq2 = deque(), deque()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dq1.append((i,j))
                if i == m-1 or j == n-1:
                    dq2.append((i,j))
        v1,v2 = set(dq1),set(dq2)
        while dq1:
            i,j = dq1.popleft()
            for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and grid[i][j] <= grid[ni][nj] and (ni,nj) not in v1:
                    dq1.append((ni,nj))
                    v1.add((ni,nj))
        while dq2:
            i,j = dq2.popleft()
            for di, dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and grid[i][j] <= grid[ni][nj] and (ni,nj) not in v2:
                    dq2.append((ni,nj))
                    v2.add((ni,nj))
        ans = []
        for i in v2:
            if i in v1:
                ans.append([i[0],i[1]])
        return ans