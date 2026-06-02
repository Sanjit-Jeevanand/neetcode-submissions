class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def cs (n):
            if n <= 1: return 1
            if n in memo: return memo[n]
            memo[n] = cs(n-1)+cs(n-2)
            return memo[n]
        return cs(n)