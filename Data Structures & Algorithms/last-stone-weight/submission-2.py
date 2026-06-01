class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for i in stones:
            heapq.heappush(h,-i)
        while len(h) > 1:
            x = heapq.heappop(h)
            y = heapq.heappop(h)
            heapq.heappush(h,x-y)
        return -h[0]