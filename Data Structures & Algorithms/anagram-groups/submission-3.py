class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        tempChars = []
        temp = ""

        for string in strs:
            tempChars = sorted(string)
            temp = ''.join(tempChars)
            if temp in d.keys():
                d[temp].append(string)
            else:
                d[temp] = [string]
        
        return list(d.values())