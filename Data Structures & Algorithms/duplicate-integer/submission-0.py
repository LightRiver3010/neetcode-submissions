class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = []
        for i in nums:
            if i not in ans:
                ans.append(i)
            else:
                return True
        return False