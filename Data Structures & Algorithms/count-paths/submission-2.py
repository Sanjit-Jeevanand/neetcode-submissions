class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int)
        def solve(i,j):
            if i == 0 or j == 0: return 1
            if i >= m or j >= n: return 0
            if (i,j) in memo: return memo[(i,j)]
            memo[(i,j)] = solve(i-1,j) + solve(i,j-1)
            return memo[(i,j)]
        return solve(m-1,n-1)