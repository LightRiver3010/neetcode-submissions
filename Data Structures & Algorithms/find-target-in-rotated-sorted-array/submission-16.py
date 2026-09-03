class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1
        M = (L + R) // 2
        if len(nums) < 3:
            if nums[L] == target:
                return L
            elif nums[R] == target:
                return R
            elif nums[M] == target:
                return M
            else:
                return -1
        while M != L and M != R:
            if nums[L] == target:
                return L
            if nums[R] == target:
                return R
            if nums[M] == target:
                return M
            if nums[L] < nums[M]:
                if target > nums[L] and target < nums[M]:
                    R = M
                else:
                    L = M
            else: #if nums[L] > nums[M]
                if target > nums[M] and target < nums[R]:
                    L = M
                else:
                    R = M
            M = (L + R) // 2
        return -1