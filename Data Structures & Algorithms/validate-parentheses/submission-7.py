class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        d = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for c in s:
            if c in d.keys():
                if len(arr) == 0 or d[c] != arr.pop():
                    return False
            else:
                arr.append(c)
        return True if len(arr) == 0 else False