class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = []
        if len(t) != len(s):
            return False
        else:
            for i in s:
                ans.append(i)
            for i in t:
                if i not in ans:
                    return False
                ans.remove(i)
        return True