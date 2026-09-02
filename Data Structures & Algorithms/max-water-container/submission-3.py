class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        currArea, maxArea = 0, 0
        while L < R:
            currArea = min(heights[L], heights[R]) * (R - L)
            maxArea = max(currArea, maxArea)
            if heights[L] >= heights[R]:
                R -= 1
            else:
                L += 1
        return maxArea