class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        closest = 0
        while l <= r:
            m = ((l + r) // 2)
            s = m * m
            if s > x:
                r = m - 1
            elif s < x:
                closest = m
                l = m + 1
            else:
                return m
        return closest