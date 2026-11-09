class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, M, R = 0, len(nums) // 2, len(nums) - 1
        while M != R and M != L:
            if nums[M] > nums[L]:
                if nums[R] < nums[L]:
                    L = M
                else:
                    return nums[L]
            else:
                R = M
            M = (L + R) // 2
        return min(nums[L], nums[R])