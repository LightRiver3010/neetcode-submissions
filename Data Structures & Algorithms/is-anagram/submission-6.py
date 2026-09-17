class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = defaultdict(int), defaultdict(int)
        for i in s:
            d1[i] += 1
        for j in t:
            d2[j] += 1
        if d1 == d2:
            return True
        return False