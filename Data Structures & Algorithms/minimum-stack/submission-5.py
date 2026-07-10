class MinStack:

    def __init__(self):
        self.stack = []
        self.smallStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.smallStack:
            val = min(val, self.smallStack[-1])
        self.smallStack.append(val)

    def pop(self) -> None:
        self.smallStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]  

    def getMin(self) -> int:
        return self.smallStack[-1]