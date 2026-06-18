class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        n = len(prices)
        def solve(i,h,s):
            if i == n: return 0
            if (i,h,s) in memo: return memo[(i,h,s)]
            if h:
                memo[(i,h,s)] = max(solve(i+1,1,0), solve(i+1,0,1) + prices[i])
            else:
                if s:
                    memo[(i,h,s)] = solve(i+1,h,0)
                else:
                    memo[(i,h,s)] = max(solve(i+1,0,0),solve(i+1,1,0) - prices[i])
            return memo[(i,h,s)]
        return solve(0,0,0)