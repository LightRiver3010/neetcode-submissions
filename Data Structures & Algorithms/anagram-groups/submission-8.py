class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        lst = []
        for s in strs:
            lst = [0] * 26
            for c in s:
                lst[ord(c) - ord("a")] += 1
            lst = tuple(lst)
            d[lst].append(s)
        return list(d.values())