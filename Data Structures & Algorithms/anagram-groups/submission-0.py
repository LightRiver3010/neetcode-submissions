class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for i in strs:
            key = ''.join(sorted(i))
            ans.setdefault(key, []).append(i)
        return list(ans.values())