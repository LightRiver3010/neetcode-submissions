class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        C, remainder = 0, 0
        d = {}
        while C < len(nums):
            remainder = target - nums[C]
            if remainder in d.keys():
                return [d[remainder], C]
            else:
                d[nums[C]] = C
            C += 1