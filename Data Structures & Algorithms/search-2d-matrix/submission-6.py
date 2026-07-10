class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L = 0
        R = 0
        M = len(matrix) // 2
        oldMs = []
        while M < len(matrix) and M not in oldMs:
            currMatrix = matrix[M]
            L = 0
            R = len(currMatrix) - 1
            oldMs.append(M)
            if target > currMatrix[L] and target > currMatrix[R]:
                M = (M + len(matrix)) // 2
            elif target < currMatrix[L] and target < currMatrix[R]:
                M = M // 2
            else:
                return self.binarySearch(currMatrix, target)
        return False

    def binarySearch(self, lst:list[int], target):
        L = 0
        R = len(lst) - 1
        midd = 0
        while L <= R:
            midd = (L + R) // 2
            if lst[midd] == target:
                return True
            elif lst[midd] < target:
                L = midd + 1
            else:
                R = midd - 1
        return False