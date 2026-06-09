class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        memo = {}
        def solve(i,j):
            if i == 0 and j ==0: return 0
            if i == 0: return j
            if j == 0: return i
            if (i,j) in memo: return memo[(i,j)]
            if w1[i-1] == w2[j-1]:
                memo[(i,j)] = solve(i-1,j-1)
                return memo[(i,j)]
            memo[(i,j)] = min(solve(i-1,j), solve(i,j-1), solve(i-1,j-1)) + 1
            return memo[(i,j)]
        return solve(len(w1),len(w2))