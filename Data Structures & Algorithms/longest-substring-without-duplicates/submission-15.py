class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        currLen, maxLen = 0, 0
        L, R = 0, 0
        while R < len(s):
            while s[R] in ss:
                ss.remove(s[L])
                L += 1
                currLen -= 1
            ss.add(s[R])
            R += 1
            currLen += 1
            if currLen > maxLen:
                maxLen = currLen
        return maxLen