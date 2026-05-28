class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        left = [False]*n
        ans = []
        def perm(curr):
            if len(curr) == n:
                ans.append(curr.copy())
            for i in range(n):
                if not left[i]:
                    curr.append(nums[i])
                    left [i] = True
                    perm(curr)
                    curr.pop()
                    left[i] = False
        perm([])
        return ans