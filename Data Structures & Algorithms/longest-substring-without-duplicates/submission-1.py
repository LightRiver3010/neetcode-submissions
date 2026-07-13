class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        R = 0
        currChars = []
        currChar = ""
        maxLength = 0
        currLength = 0
        while R < len(s):
            currChar = s[R]
            while currChar in currChars:
                currChars.pop(0)
            currChars.append(currChar)
            currLength = len(currChars)
            if currLength > maxLength:
                maxLength = currLength
            R += 1
        return maxLength