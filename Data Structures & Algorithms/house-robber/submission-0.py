class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        memo = {0: nums[0], 1: max(nums[0],nums[1])}
        def rb(i):
            if i in memo: return memo[i]
            memo[i] = max(nums[i]+rb(i-2), rb(i-1))
            return memo[i]
        return rb(n-1)