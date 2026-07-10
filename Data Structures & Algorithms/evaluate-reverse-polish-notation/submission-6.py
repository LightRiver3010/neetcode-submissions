class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        total = 0
        for i in tokens:
            if i == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                total = num1 + num2
                stack.append(total)
            elif i == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                total = num2 - num1
                stack.append(total)
            elif i == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                total = num1 * num2
                stack.append(total)
            elif i == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                total = int(num2 / num1)
                stack.append(total)
            else:
                stack.append(int(i))
        return int(stack[0])