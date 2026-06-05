class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def solve(i, W):
            if W == amount: return 1
            if W > amount: return 0
            if i == len(coins): return 0
            if (i, W) in memo: return memo[(i, W)]
            memo[(i, W)] = (solve(i + 1, W) + solve(i, W + coins[i]))
            return memo[(i, W)]
        return solve(0, 0)