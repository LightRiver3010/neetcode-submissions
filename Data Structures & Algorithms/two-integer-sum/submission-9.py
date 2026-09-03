class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        C = 0
        d = {}
        toFind = 0
        while True:
            toFind = target - nums[C]
            if toFind in d.keys():
                return [d[toFind], C]
            d[nums[C]] = C
            C += 1