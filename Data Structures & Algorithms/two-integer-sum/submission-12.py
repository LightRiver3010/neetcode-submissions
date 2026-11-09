class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        R = 0
        d = {}
        while R < len(nums):
            if nums[R] in d.values():
                for i in d.keys():
                    if d[i] == nums[R]:
                        return [i, R]
            d[R] = target-nums[R]
            R += 1
        return []