class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R, currMax, maxMax = 0, len(heights)-1, 0, 0
        while L < R:
            currMax = (min(heights[L], heights[R])) * (R - L)
            maxMax = max(maxMax, currMax)
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1
        return maxMax