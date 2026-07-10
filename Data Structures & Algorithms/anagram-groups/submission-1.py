class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            sortedStr = ''.join(sorted(i))
            ans[sortedStr].append(i)
        return list(ans.values())