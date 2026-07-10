class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = L + 1
        while L < R:
            if R >= len(numbers):
                L += 1
                R = L + 1
            total = numbers[L] + numbers[R]
            if total == target:
                return [L+1, R+1]
            R += 1
        return [-1, -1]