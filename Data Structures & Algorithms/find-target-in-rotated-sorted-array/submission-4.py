class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            M = (R + L) // 2
            if nums[M] == target:
                return M
            if nums[L] == target:
                return L
            if nums[R] == target:
                return R
            if R - L == 1:
                return -1
            if nums[L] <= nums[M]:
                if nums[M] < target or nums[L] > target:
                    L = M + 1
                else:
                    R = M - 1
            else:
                if nums[M] > target or nums[R] < target:
                    R = M - 1
                else:
                    L = M + 1
        return -1