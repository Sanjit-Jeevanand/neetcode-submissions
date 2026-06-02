class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        memo = {}
        def cc(W):
            if W == 0:
                return 0
            if W < 0:
                return float('inf')
            if W in memo: return memo[W]
            memo[W] = float('inf')
            for x in coins:
                memo[W] = min(cc(W-x) + 1, memo[W])
            return memo[W]
        ans = cc(amount) 
        return ans if ans != float('inf') else -1