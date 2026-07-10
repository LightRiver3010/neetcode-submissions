class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        n = len(temperatures)
        for i in range(len(temperatures)):
            temp = i + 1
            while temp < n and temperatures[i] >= temperatures[temp]:
                temp += 1
            if temp > n - 1:
                result.append(0)
            else:
                result.append(temp - i)
        return result