class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        t = 0
        h = [(grid[0][0],0,0)]
        visited = {(0,0)}
        while h:
            while h[0][0] <= t:
                x,i,j = heapq.heappop(h)
                if i == n-1 and j == n-1:
                    return max(x,t)
                for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
                    ni, nj = i+di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        if (ni,nj) not in visited:
                            visited.add((ni,nj))
                            heapq.heappush(h,(grid[ni][nj],ni,nj))
            t += 1