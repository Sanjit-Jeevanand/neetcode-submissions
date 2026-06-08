class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        memo = {}
        def solve(i,j):
            if i == 0 or j == 0: return 0
            if (i,j) in memo: return memo[(i,j)]
            if t1[i-1] == t2[j-1]:
                memo[(i,j)] = solve(i-1,j-1) + 1
            else:
                memo[(i,j)] = max(solve(i-1,j), solve(i,j-1))
            return memo[(i,j)]
        return solve(len(t1),len(t2))