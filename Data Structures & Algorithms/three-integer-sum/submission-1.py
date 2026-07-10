class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        seen = []
        a = 0
        while a < len(nums)-2:
            if nums[a] in seen:
                a += 1
                continue
            c = len(nums)-1
            b = a + 1
            while b < c:
                total = nums[a] + nums[b] + nums[c]
                if total < 0:
                    b += 1
                elif total > 0:
                    c -= 1
                else:
                    ans.append([nums[a], nums[b], nums[c]])
                    seen.append(nums[a])
                    b += 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
            a += 1
        return ans