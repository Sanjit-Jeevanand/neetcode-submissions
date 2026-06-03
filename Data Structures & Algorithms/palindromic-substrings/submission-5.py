class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = {}
        def cs(i,j):
            if i > j: return True
            if i == j : 
                memo[(i,j)] = True
                return memo[(i,j)]
            if (i,j) in memo: return memo[(i,j)]
            if j-i+1 <= 1:
                memo[(i,j)] = True
                return memo[(i,j)]
            if s[i] == s[j] and cs(i+1,j-1):
                memo[(i,j)] = True
                return memo[(i,j)]
            else:
                memo[(i,j)] = False
                return memo[(i,j)]
        ans = 0
        for i in range(n):
            for j in range(i,n):
                if cs(i,j):
                    ans += 1
        return ans