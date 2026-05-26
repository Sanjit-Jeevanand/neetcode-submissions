class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for i in t:
            d[i] += 1
        l = 0
        ans = ""
        n = len(s)
        for i in range(n):
            if s[i] in d:
                d[s[i]] -= 1
                if all(d[x] <= 0 for x in d): 
                    while any(d[x] < 0 for x in d) and l < n:
                        while s[l] not in d:
                            l += 1
                        if s[l] in d and d[s[l]] < 0:
                            d[s[l]] += 1
                            l += 1
                        else:
                            break
                    while s[l] not in d:
                            l += 1
                    if i-l+1 < len(ans) or len(ans) == 0:
                        ans = s[l:i+1]  
        return ans