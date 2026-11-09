class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        L, M, R = 0, 0, 0
        ans = []
        while L < len(nums) - 2:
            if L > 0 and nums[L-1] == nums[L]:
                L += 1
                continue
            M = L + 1
            R = len(nums) - 1
            while M < R:
                currSum = nums[R] + nums[M]
                if (currSum == -nums[L]):
                    ans.append([nums[L], nums[M], nums[R]])
                    R -= 1
                    while nums[R] == nums[R + 1]:
                        if R < M:
                            break
                        R -= 1
                elif (currSum > -nums[L]):
                    R -= 1
                else:
                    M += 1
            L += 1
        return ans