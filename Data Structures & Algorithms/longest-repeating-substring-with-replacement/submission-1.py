class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        d = defaultdict(int)
        l = 0
        for i in range(n):
            d[s[i]] += 1
            if max(d.values()) + k < sum(d.values()):
                d[s[l]] -= 1
                l += 1
            ans = max(ans,sum(d.values()))
        return ans