class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R, currLen, maxLen, count = 0, 0, 0, 0, 0
        d = {}
        while R < len(s):
            while R < len(s):
                count = d.get(s[R], 0)
                if count == 0:
                    d[s[R]] = 1
                    R += 1
                else:
                    break
            currLen = R - L
            if currLen > maxLen:
                maxLen = currLen
            del d[s[L]]
            L += 1
        return maxLen
            