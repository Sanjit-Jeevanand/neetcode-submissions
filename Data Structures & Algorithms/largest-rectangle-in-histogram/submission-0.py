class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        h.append(0)
        n = len(h)
        s = []
        ans = 0
        for i in range(len(h)):
            while s and h[i] < h[s[-1]]:
                x = h[s.pop()]
                if s:
                    w = i - s[-1] - 1
                else:
                    w = i
                ans = max(ans,w*x)
            s.append(i)
        return ans