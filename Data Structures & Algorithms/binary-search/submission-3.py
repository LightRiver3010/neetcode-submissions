class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1
        while L <= R:
            midd = ((L + R) // 2)
            if nums[midd] == target:
                return midd
            elif nums[midd] > target:
                R = midd - 1
            else:
                L = midd + 1
        return -1