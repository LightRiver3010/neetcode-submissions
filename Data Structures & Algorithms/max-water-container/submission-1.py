class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        largest = 0
        currArea = 0
        while L < R:
            smallest = min(heights[L], heights[R])
            currArea = smallest * (R - L)
            if currArea > largest:
                largest = currArea
            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        return largest