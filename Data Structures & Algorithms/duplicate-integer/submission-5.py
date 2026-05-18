class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set()
        for i in range(len(nums)):
            arr.add(nums[i])
            print(arr)
        if len(arr) != len(nums):
            return True
        return False