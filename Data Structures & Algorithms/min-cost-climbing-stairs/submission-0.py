class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {0: 0, 1: 0}
        def mcc(i):
            if i in memo: return memo[i]
            memo[i] = min(mcc(i-1) + cost[i-1], mcc(i-2) + cost[i-2])
            return memo[i]
        return mcc(n)