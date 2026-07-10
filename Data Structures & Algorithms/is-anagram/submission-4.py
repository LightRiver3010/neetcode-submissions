class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        for i in s:
            sDict[i] = sDict.get(i, 0) + 1
        for i in t:
            tDict[i] = tDict.get(i, 0) + 1
        return sDict == tDict