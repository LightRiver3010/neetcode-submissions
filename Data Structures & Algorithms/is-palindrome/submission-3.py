class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        L = 0
        R = len(s)-1
        while L < R:
            if not s[L].isalnum():
                L += 1
            elif not s[R].isalnum():
                R -= 1
            else:
                if s[L] != s[R]:
                    return False
                L += 1
                R -= 1
        return True