class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        self.currMin = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.currMin = self.minStack[-1]
        else:
            self.currMin = None
        if self.currMin == None or self.currMin > val:
            self.currMin = val
        self.minStack.append(self.currMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
