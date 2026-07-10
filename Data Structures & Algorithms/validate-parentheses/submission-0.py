class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []
        for i in s:
            if i in chars:
                if stack and stack[-1] == chars[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        return False