class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        n = len(nums)
        def combs(curr, start, s):
            if s == target:
                ans.append(curr.copy())
                return
            for i in range(start,n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                if s + nums[i] <= target:
                    curr.append(nums[i])
                    combs(curr, i+1, s+nums[i])
                    curr.pop()
        combs([],0,0)
        return ans