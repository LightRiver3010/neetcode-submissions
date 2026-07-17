class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carArr = position.copy()
        numIterations = []
        toGo = 0
        numIteration = 0
        currIterations = 0
        prevIterations = 0

        for i in range(len(position)):
            carArr[i] = [position[i], speed[i]]
        carArr.sort(key = lambda x: x[0])

        for j in range(len(carArr)):
            toGo = target - carArr[j][0]
            numIteration = toGo/carArr[j][1]
            carArr[j] = numIteration
        
        stack = []
        while carArr:
            stack.append(carArr.pop())
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
