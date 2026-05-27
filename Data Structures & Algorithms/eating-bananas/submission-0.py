class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can(x):
            t = 0
            for i in piles:
                t += math.ceil(i/x)
            return t <= h
        l = 1
        r = max(piles)
        while l < r:
            m = (l+r)//2
            if can(m):
                r = m
            else:
                l = m+1
        return r