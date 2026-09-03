class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 0
        maxProfit = 0
        while R < len(prices):
            if prices[R] >= prices[L]:
                maxProfit = max((prices[R] - prices[L]), maxProfit)
            else:
                L = R
            R += 1
        return maxProfit