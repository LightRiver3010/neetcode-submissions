class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ans = ""
        for i in s:
            if i.isalnum():
                ans += i
        l = 0
        r = len(ans)-1
        while l < r:
            if ans[l] != ans[r]:
                return False
            l += 1
            r -= 1
        return True