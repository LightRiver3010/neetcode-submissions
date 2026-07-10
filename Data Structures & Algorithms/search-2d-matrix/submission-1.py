class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a, b = 0, len(matrix) -1

        row = None
        while a <= b and row == None:
            l = matrix[a]
            r = matrix[b]
            if target <= l[-1]:
                row = a
            elif target >= r[0]:
                row = b
            else:
                a += 1
                b -= 1
        if row is None:
            return False
        l = 0
        r = len(matrix[row])-1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False