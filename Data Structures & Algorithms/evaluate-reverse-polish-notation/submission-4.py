class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == "+":
                x = s.pop()
                s[-1]+= x
            elif i == "-":
                x = s.pop()
                s[-1] -= x
            elif i == "*":
                x = s.pop()
                s[-1] *= x
            elif i == "/":
                x = s.pop()
                s[-1] = int(s[-1]/x)
            else:
                s.append(int(i))
        return s[-1]