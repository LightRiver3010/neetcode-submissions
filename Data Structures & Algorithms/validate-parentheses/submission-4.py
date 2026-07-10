class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = []
        if len(s) % 2 != 0:
            return False
        for char in s:
            if char in d.keys():
                if len(stack) == 0:
                    return False
                if stack[-1] != d[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        
        return True if len(stack) == 0 else False