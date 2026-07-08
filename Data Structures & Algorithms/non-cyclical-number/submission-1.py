class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        x = 0
        while n:
            x += (n%10)**2
            n //= 10
            if (n == 1 and x == 0) or (x == 1 and n ==0):
                return True
            if n == 0:
                n = x
                if x in visited: return False
                else: 
                    visited.add(x)
                    x = 0
        