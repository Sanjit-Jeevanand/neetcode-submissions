class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        ans = []
        left = [False]*n
        def subs(curr, start):
            ans.append(curr.copy())
            for i in range(start, n):
                if i > 0 and nums[i] == nums[i-1] and not left[i-1]:
                    continue
                curr.append(nums[i])
                left[i] = True
                subs(curr, i+1)
                left[i] = False
                curr.pop()
        subs([],0)
        return ans