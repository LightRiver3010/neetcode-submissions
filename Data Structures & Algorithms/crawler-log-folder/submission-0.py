class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        i = 0
        while i < len(logs):
            if logs[i] == "../":
                if stack:
                    stack.pop()
            elif logs[i] == "./":
                pass
            else:
                stack.append(1)
            i += 1
        i = 0
        while stack:
            i += 1
            stack.pop()
        return i
        