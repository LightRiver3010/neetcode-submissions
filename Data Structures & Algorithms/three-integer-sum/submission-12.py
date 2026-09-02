class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        L, C = 0, 0
        ans = []
        d = {}
        toFind = 0
        target = 0
        while L < len(nums)-2:
            C = L + 1
            d = {}
            target = 0 - nums[L]
            while C < len(nums):
                toFind = target - nums[C]
                if toFind in d.keys():
                    ans.append([nums[L], toFind, nums[C]])
                    C += 1
                    while C < len(nums) and nums[C] == nums[C-1]:
                        C += 1
                else:
                    d[nums[C]] = C
                    C += 1
            L += 1
            while L < len(nums) and nums[L] == nums[L-1]:
                L += 1
        return ans