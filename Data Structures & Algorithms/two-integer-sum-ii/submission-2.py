class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R, currSum = 0, len(numbers)-1, 0
        while L < R:
            currSum = numbers[R] + numbers[L]
            if currSum == target:
                return [L+1, R+1]
            elif currSum > target:
                R -= 1
            else:
                L += 1