class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        L = 0
        M = L + 1
        R = len(nums) - 1
        while L < len(nums) - 2:
            while L > 0 and L < len(nums) - 2 and nums[L] == nums[L-1]:
                L += 1
                M = L + 1
                R = len(nums) - 1
                continue
            if M >= len(nums) - 1 or M >= R:
                L += 1
                M = L + 1
                R = len(nums) - 1
                continue
            total = nums[L] + nums[M] + nums[R]
            if total > 0:
                R -= 1
            elif total < 0:
                M += 1
            else:
                ans.append([nums[L], nums[M], nums[R]])
                M += 1
                R -= 1
                while M < R and nums[M] == nums[M-1]:
                    M += 1
        return ans
