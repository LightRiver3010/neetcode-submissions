class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1
        M = (L + R) // 2
        if nums[M] == target:
            return M
        if nums[R] == target:
            return R
        if nums[L] == target:
            return L
        while M != L and M != R:
            if nums[M] == target:
                return M
            elif nums[R] == target:
                return R
            elif nums[L] == target:
                return L
            else:
                if nums[L] < nums[M]:
                    if target < nums[M] and target > nums[L]:
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