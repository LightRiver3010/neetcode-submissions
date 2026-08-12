class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L, R = 0, 0
        d1, d2 = {}, {}
        while R < len(s1):
            if s1[R] in d1.keys():
                d1[s1[R]] += 1
            else:
                d1[s1[R]] = 1
            R += 1
        R = 0
        while R < len(s2):
            while True:
                if R >= len(s2):
                    break
                if s2[R] in d2.keys():
                    d2[s2[R]] += 1
                else:
                    d2[s2[R]] = 1
                if (R - L) >= len(s1)-1:
                    break
                R += 1
            if d1 == d2:
                return True
            if d2[s2[L]] == 1:
                del d2[s2[L]]
            else:
                d2[s2[L]] -= 1
            L += 1
            R += 1
        return False