class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        x = prices[0]
        for i in prices:
            if x < i:
                ans = max(ans,i-x)
            else:
                x = i
        return ans