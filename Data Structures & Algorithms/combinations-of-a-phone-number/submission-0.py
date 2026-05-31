class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dtl = {'2': ["a","b","c"], '3': ["d","e","f"],
        '4': ["g","h","i"],'5': ["j","k","l"],'6': ["m","n","o"],'7': ["p","q","r", "s"],
        '8': ["t","u","v"],'9': ["w","x","y", "z"]}
        n = len(digits)
        if n == 0:return[]
        ans = []
        def dfs(i,s):
            if len(s) == n:
                ans.append(s)
                return
            for x in dtl[digits[i]]:
                dfs(i+1,s+x)
        dfs(0,"")
        return ans