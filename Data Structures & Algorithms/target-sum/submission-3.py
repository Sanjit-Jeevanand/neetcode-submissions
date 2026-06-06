class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        S = sum(nums)
        W = S - target
        if W % 2 == 1: return 0
        W //= 2
        memo = {}
        n = len(nums)
        def solve(i,W):
            if W < 0: return 0
            if i == 0:
                return 1 if W == 0 else 0
            if (i,W) in memo: return memo[(i,W)]
            memo[(i,W)] = solve(i-1,W) + solve(i-1,W-nums[i-1])
            return memo[(i,W)]
        return solve(n,W)