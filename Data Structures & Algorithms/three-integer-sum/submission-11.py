class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        L, M, R, currTarget, currSum = 0, 0, 0, 0, 0
        triplets = []
        while L < len(nums)-2:
            R = len(nums)-1
            M = L + 1
            while M < R:
                currTarget = -nums[L]
                currSum = nums[R] + nums[M]
                if currSum < currTarget:
                    M += 1
                    while nums[M-1] == nums[M] and M < R:
                        M += 1
                elif currSum > currTarget:
                    R -= 1
                else: #if currSum == currTarget
                    triplets.append([nums[L], nums[M], nums[R]])
                    M += 1
                    while nums[M-1] == nums[M] and M < R:
                        M += 1
            L += 1
            while nums[L-1] == nums[L] and L < len(nums)-2:
                L += 1
        return triplets