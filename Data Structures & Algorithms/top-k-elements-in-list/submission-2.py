class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if (not nums) or (k == 0):
            return []
        ans = {}
        anss = []
        for i in nums:
            if i in ans:
                ans[i] += 1
            else:
                ans[i] = 1
        ans2 = sorted(ans.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            anss.append(ans2[i][0])
        return anss
                
            
        