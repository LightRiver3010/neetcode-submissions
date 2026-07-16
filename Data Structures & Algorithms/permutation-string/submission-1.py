class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L = 0
        R = 0
        d1 = {}
        d2 = {}

        if len(s1) > len(s2):
            return False

        while R < len(s1):
            if s1[R] in d1.keys():
                d1[s1[R]] += 1
            else:
                d1[s1[R]] = 1
            if s2[R] in d2.keys():
                d2[s2[R]] += 1
            else:
                d2[s2[R]] = 1
            R += 1

        R -= 1
        while R < len(s2):
            if d1 == d2:
                return True
            d2[s2[L]] -= 1
            if d2[s2[L]] == 0:
                del d2[s2[L]]
            L += 1
            R += 1
            if R < len(s2):
                if s2[R] in d2.keys():
                    d2[s2[R]] += 1
                else:
                    d2[s2[R]] = 1
        return False