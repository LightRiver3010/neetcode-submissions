class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if (not nums) or (not k):
            return []
        numcount = {}
        answer = []
        count = 0
        for i in nums:
            if i in numcount:
                numcount[i] += 1
            else:
                numcount[i] = 1
        numcount = sorted(numcount.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            answer.append(numcount[i][0])
        return answer