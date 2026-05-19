class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        n = len(s1)
        for i in s1:
            d1[i] += 1
        for i in range(len(s2)):
            d2[s2[i]] += 1
            if i >= n:
                d2[s2[i-n]] -= 1
            if all(d1[x] == d2[x] for x in d1):
                return True
        return False
        