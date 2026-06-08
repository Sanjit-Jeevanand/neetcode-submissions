class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n,o = len(s1), len(s2), len(s3)
        if m+n != o: return False
        memo = {}
        def solve(i,j):
            if i == 0 or j == 0: return True if s1[:i] + s2[:j] == s3[:i+j] else False
            if (i,j) in memo: return memo[(i,j)]
            memo[(i,j)] = False
            if s1[i-1] == s3[i+j-1] and solve(i-1,j):   memo[(i,j)] = True
            if s2[j-1] == s3[i+j-1] and solve(i,j-1):   memo[(i,j)] = True
            return memo[(i,j)]
        return solve(m,n)