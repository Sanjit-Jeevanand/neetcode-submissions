class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = {}
        ans = ""
        if n == 1: return s
        def lp(i,x):
            nonlocal ans
            if i > x:
                return True
            if (i,x) in memo: return memo[(i,x)]
            if x-i+1 == 1:
                memo[(i,x)] = True
                if x-i+1 > len(ans):
                    ans = s[i:x+1]
            elif s[i] == s[x] and lp(i+1,x-1):
                memo[(i,x)] = True
                if x-i+1 > len(ans):
                    ans = s[i:x+1]
            else:
                memo[(i,x)] = False
                lp(i+1,x)
                lp(i,x-1)
            return memo[(i,x)]
        lp(0,n-1)
        return ans