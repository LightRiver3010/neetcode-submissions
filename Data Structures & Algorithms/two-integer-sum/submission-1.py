class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = 0
        R = 1
        while L < R:
            if R == len(nums):
                L += 1
                R = L + 1
            total = nums[L] + nums[R]
            if total == target:
                return [L, R]
            else:
                R += 1
        