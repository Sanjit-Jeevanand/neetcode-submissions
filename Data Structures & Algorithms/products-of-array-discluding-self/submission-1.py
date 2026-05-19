class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l1 = [1]*(n+1)
        l2 = [1]*(n+1)
        for i in range(1,n+1):
            l1[i] *= nums[i-1]*l1[i-1]
        for i in range(n-2,-1,-1):
            l2[i] *= nums[i+1]*l2[i+1]
        for i in range(n):
            l1[i] *= l2[i]
        return l1[:n]