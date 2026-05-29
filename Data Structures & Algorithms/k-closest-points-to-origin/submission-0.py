class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x,y in points:
            heapq.heappush(h,(-math.sqrt((x)**2 + (y)**2),x,y))
            if len(h) > k:
                heapq.heappop(h)
        ans = []
        for _,x,y in h:
            ans.append([x,y])
        return ans