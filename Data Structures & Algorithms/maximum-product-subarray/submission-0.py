class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def mp(i,j):
            if i > j: return - float('inf')
            if j < 0 or i < 0: return nums[0]
            if i == j: 
                memo[(i,j)] = nums[i]
                return memo[(i,j)]
            if (i,j) in memo: return memo[(i,j)]
            memo[(i,j)] = mp(i,j-1) * nums[j]
            return memo[(i,j)]
        for i in range(n):
            for j in range(n):
                mp(i,j)
        return max(memo.values())