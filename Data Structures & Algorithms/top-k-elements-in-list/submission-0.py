class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        h = []
        for i in d:
            heapq.heappush(h,(d[i],i))
            if len(h) > k:
                heapq.heappop(h)
        return [x[1] for x in h]