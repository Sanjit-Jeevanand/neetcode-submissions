class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(x):
            return x == x[::-1]
        ans = []
        n = len(s)
        def palpart(start, curr):
            if start == n:
                ans.append(curr.copy())
            for i in range(start+1, n+1):
                if isPal(s[start: i]):
                    curr.append(s[start:i])
                    palpart(i, curr)
                    curr.pop()
        palpart(0,[])
        return ans