class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        n = len(nums)
        def combs(curr, start, s):
            if s == target:
                ans.append(curr.copy())
            for i in range(start,n):
                if s + nums[i] <= target:
                    curr.append(nums[i])
                    combs(curr, i, s+nums[i])
                    curr.pop()
        combs([],0,0)
        return ans