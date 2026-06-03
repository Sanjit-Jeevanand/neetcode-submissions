class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = {}
        def isPal(i, j):
            if i >= j:
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = (s[i] == s[j] and isPal(i + 1, j - 1))
            return memo[(i, j)]
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if isPal(i, j):
                    ans += 1
        return ans