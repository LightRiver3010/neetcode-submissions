class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        M = 0
        while L <= R:
            M = (L + R) // 2
            if nums[L] == target:
                return L
            elif nums[R] == target:
                return R
            elif nums[M] == target:
                return M
            else:
                if nums[M] >= nums[L]:
                    if target < nums[L] or target > nums[M]:
                        L = M + 1
                    else:
                        R = M - 1
                else: #nums[M] < nums[L]
                    if target > nums[R] or target < nums[M]:
                        R = M - 1
                    else:
                        L = M + 1
        return -1