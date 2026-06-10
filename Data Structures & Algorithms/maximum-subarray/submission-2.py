class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        ans = nums[0]
        for i in range(1,len(nums)):
            if s < 0:
                s = 0
            s = s + nums[i]
            ans = max(ans,s)
        return ans