class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for i in s:
            count = 1
            if i - 1 not in s:
                while i+1 in s:
                    i += 1
                    count += 1
            ans = max(ans, count)
        return ans