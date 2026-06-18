class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = 0
        for i in digits:
            n += i
            n *= 10
        n //= 10
        n += 1
        dq = deque([])
        while n:
            dq.appendleft(n%10)
            n //= 10
        return list(dq)