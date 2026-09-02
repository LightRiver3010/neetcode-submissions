class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            iCopy = str(sorted(i))
            if iCopy in d.keys():
                d[iCopy].append(i)
            else:
                d[iCopy] = [i]
        return list(d.values())