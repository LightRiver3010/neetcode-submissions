class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1, d2 = defaultdict(int), defaultdict(int)
        C = 0
        while C < len(s):
            d1[s[C]] += 1
            d2[t[C]] += 1
            C += 1
        if d1 == d2:
            return True
        return False