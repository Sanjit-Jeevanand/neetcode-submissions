class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        def rob1(i,n):
            x = len(nums[i:n+1])
            if x == 1: return nums[i]
            memo = { i: nums[i], i+1: max(nums[i], nums[i+1])}
            def rb(i):
                if i in memo: return memo[i]
                memo[i] = max(rb(i-2)+nums[i], rb(i-1))
                return memo[i]
            return rb(n)
        return max(rob1(1,n-1),rob1(0,n-2))