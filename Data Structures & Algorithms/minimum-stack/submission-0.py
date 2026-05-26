class MinStack:

    def __init__(self):
        self.s = []
        self.mini = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.mini:
            self.mini.append(min(val,self.mini[-1]))
        else:
            self.mini.append(val)
        
    def pop(self) -> None:
        self.s.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mini[-1]