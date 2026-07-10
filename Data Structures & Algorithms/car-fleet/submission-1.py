class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Creating arrays for each car
        carrArr = []
        for i in range(len(position)):
            carrArr.append([position[i], speed[i]])
        carrArr.sort(key=lambda x: x[0], reverse=True)

        currIterations = 99999
        prevIterations = 0
        numIterations = []
        for j in carrArr:
            toGo = target - j[0]
            currIterations = toGo/j[1]
            if currIterations < prevIterations:
                currIterations = prevIterations
            numIterations.append(currIterations)
            prevIterations = currIterations

        return (len(list(set(numIterations))))