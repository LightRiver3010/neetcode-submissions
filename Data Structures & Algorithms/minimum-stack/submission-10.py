class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.currMin = None

    def push(self, val: int) -> None:
        if len(self.minStack) == 0:
            self.currMin = None
        else:
            self.currMin = self.minStack[-1]
        if self.currMin == None or val < self.currMin:
            self.currMin = val
        self.stack.append(val)
        self.minStack.append(self.currMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]