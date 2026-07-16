class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 00 01 02 03
        # 40 41 42 43
        # 80 81 82 83
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            curR, curC = mid // len(matrix[0]), mid % len(matrix[0])
            if matrix[curR][curC] < target:
                l = curR * len(matrix[0]) + curC + 1
            elif matrix[curR][curC] > target:
                r = curR * len(matrix[0]) + curC - 1
            else:
                return True

        return False