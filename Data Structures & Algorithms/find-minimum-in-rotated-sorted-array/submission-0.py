class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        oldL = 0
        if nums[0] < nums[len(nums)- 1]:
            return nums[0]
        while R - L > 1:
            if nums[L] > nums[R]:
                oldL = L
                L = (R + L) // 2
                if nums[L] < nums[oldL]:
                    R = L
                    L = oldL
        return nums[R]