class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R, curr, maxx = 0, 0, 0, 0
        while R < len(prices):
            curr = prices[R] - prices[L]
            if curr > maxx:
                maxx = curr
            if prices[L] > prices[R]:
                L = R
                R = L + 1
            else:
                R += 1
        return maxx