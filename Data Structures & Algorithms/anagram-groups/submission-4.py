class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            sortt = str(sorted(s))
            if sortt in d.keys():
                d[sortt].append(s)
            else:
                d[sortt] = [s]
        return list(d.values())