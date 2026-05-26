class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == "+":
                x = s.pop()
                y = s.pop()
                s.append(x+y)
            elif i == "-":
                x = s.pop()
                y = s.pop()
                s.append(y-x)
            elif i == "*":
                x = s.pop()
                y = s.pop()
                s.append(x*y)
            elif i == "/":
                x = s.pop()
                y = s.pop()
                s.append(int(y/x))
            else:
                s.append(int(i))
        return s[-1]