class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R, M = 0, len(nums)-1, 0
        M = (L + R) // 2
        while M != R and M != L:
            if nums[L] > nums[M]:
                if nums[M] < nums[R]:
                    R = M
                else:
                    L = M
            else:
                if nums[R] < nums[L]:
                    L = M
                else:
                    R = M
            M = (L + R) // 2
        return min(nums[L], nums[R])