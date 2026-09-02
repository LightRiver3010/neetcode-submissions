class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        toFind = 0
        for i in range(len(nums)):
            toFind = target - nums[i]
            if toFind in d.keys():
                return [d[toFind], i]
            else:
                d[nums[i]] = i