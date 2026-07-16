class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        R = 0
        currLen = 0
        maxLen = 1
        d = {}
        currMaxChar = 0

        d[s[R]] = 1

        while R < len(s):
            currMaxChar = max(d.values())
            currLen = sum(d.values())
            if currLen - currMaxChar > k:
                d[s[L]] -= 1
                L += 1
                continue
            else:
                if currLen > maxLen:
                    maxLen = currLen
                R += 1
                if R < len(s):
                    if s[R] in d.keys():
                        d[s[R]] += 1
                    else:
                        d[s[R]] = 1
                continue
        return maxLen