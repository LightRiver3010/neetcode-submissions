class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return min(nums)
        L, R = 0, len(nums)-1
        M = (L + R) // 2
        while M != R and M != L:
            if nums[L] > nums[R]:
                if nums[M] > nums[L]:
                    L = M
                else:
                    R = M
            else:
                return nums[L]
            M = (L + R) // 2
        return nums[R]