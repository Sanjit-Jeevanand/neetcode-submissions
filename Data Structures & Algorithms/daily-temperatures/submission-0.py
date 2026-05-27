class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        s = []
        n = len(temp)
        ans = [0]*n
        for i in range(n):
            while s and temp[i] > temp[s[-1]]:
                idx = s.pop()
                ans[idx] = i - idx
            s.append(i)
        return ans