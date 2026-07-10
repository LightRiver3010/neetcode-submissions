class Solution:
    def maxArea(self, heights: List[int]) -> int:
        cur = 0
        biggest = 0
        l = 0
        r = len(heights)-1
        while l < r:
            limiting = min(heights[l], heights[r])
            cur = limiting * (r - l)
            if cur > biggest:
                biggest = cur
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return biggest
            