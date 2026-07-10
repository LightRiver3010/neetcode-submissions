class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = temperatures.copy()
        tempStack = []
        n = len(temperatures) #Using n so the value doesn't get changed as we pop from temperatures
        for j in range(n):
            currTemp = temperatures.pop()
            for i in range(len(tempStack)):
                if tempStack[-i-1] > currTemp:
                    result[-j-1] = i+1
                    break
            if result[-j-1] == currTemp: #If it's still the temperature, it hasn't been updated from the .copy()
                result[-j-1] = 0
            tempStack.append(currTemp)
        return result