class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 0 1 2  3
        # 4 5 6  7
        # 8 9 10 11
        l, r = 0, len(matrix) * len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            curR, curC = mid // len(matrix[0]), mid % len(matrix[0])
            if matrix[curR][curC] < target:
                l = mid + 1
            elif matrix[curR][curC] > target:
                r = mid - 1
            else:
                return True

        return False