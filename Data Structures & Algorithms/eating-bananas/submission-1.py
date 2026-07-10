class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m_min = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            h_temp = 0
            m = (l + r) // 2
            for i in piles:
                h_temp += math.ceil(i / m)
            if h_temp <= h:
                m_min = min(m_min, m)
                r = m - 1
            elif h_temp > h:
                l = m + 1
        return m_min