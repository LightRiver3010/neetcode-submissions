class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        L = 0
        M = L + 1
        R = len(nums) - 1
        ans = []
        while L < len(nums) - 2:
            while L > 0 and nums[L - 1] == nums[L] and L < len(nums) - 2:
                L += 1
                M = L + 1
                R = len(nums) - 1
                continue
            if M >= R:
                L += 1
                M = L + 1
                R = len(nums) - 1
                continue
            twoSum = nums[M] + nums[R]
            if twoSum > -nums[L]:
                R -= 1
                continue
            elif twoSum < -nums[L]:
                M += 1
                continue
            else:
                ans.append([nums[L], nums[M], nums[R]])
                M += 1
                while M < R and nums[M] == nums[M - 1]:
                    M += 1
        return ans