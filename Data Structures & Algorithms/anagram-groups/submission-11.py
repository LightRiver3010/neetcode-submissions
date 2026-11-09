class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        charArr = []
        for s in strs:
            charArr = [0] * 26
            for c in s:
                charArr[ord(c) - ord('a')] += 1
            charArr = tuple(charArr)
            if charArr in d.keys():
                d[charArr].append(s)
            else:
                d[charArr] = [s]
        return list(d.values())