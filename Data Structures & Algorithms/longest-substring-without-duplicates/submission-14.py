class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R = 0, 0
        maxLen = 0
        d = defaultdict(int)
        while R < len(s):
            while s[R] in d.keys() and L < R:
                if d[s[L]] > 1:
                    d[s[L]] -= 1
                else:
                    del d[s[L]]
                L += 1
            d[s[R]] += 1
            R += 1
            maxLen = max(maxLen, (R - L))
        return maxLen