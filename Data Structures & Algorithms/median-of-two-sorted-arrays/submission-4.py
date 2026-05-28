class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        small = []
        large = []
        for i in nums1:
            heapq.heappush(small,-i)
            if large and large[0] < -small[0]:
                heapq.heappush(large, -heapq.heappop(small))
            if len(small) > len(large) + 1:
                heapq.heappush(large, -heapq.heappop(small))
            if len(large) > len(small):
                heapq.heappush(small, -heapq.heappop(large))
        if len(small) > len(large):
            return -small[0]
        return (large[0] - small[0])/2
        