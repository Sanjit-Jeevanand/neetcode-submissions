class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        memo = {}
        W = sum(stones)//2
        def lsw(i, W):
            if i < 0:
                return 0
            if (i,W) in memo: return memo[(i,W)]
            take = 0
            if stones[i] <= W:
                take = stones[i] + lsw(i-1,W-stones[i])
            skip = lsw(i-1,W)
            memo[(i,W)] = max(take,skip)
            return memo[(i,W)]
        best = lsw(len(stones)-1, W)
        return sum(stones) - 2*best