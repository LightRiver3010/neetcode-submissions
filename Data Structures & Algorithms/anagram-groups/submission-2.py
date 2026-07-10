class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for idx in range(len(strs)):
            temp = str(sorted(strs[idx]))
            if temp in d.keys():
                d[temp].append(strs[idx])
            else:
                d[temp] = [strs[idx]]
        ans = []
        for combo in d.keys():
            ans.append(d[combo])
        return ans