class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S%2 == 1: return False
        S //= 2
        n = len(nums)
        memo = {}
        def solve(i,W):
            if W < 0 or i <= 0: return False
            if W == 0: return True
            if (i,W) in memo: return memo[(i,W)]
            memo[(i,W)] = solve(i-1,W) or solve(i-1, W-nums[i-1])
            return memo[(i,W)]
        return solve(n,S)