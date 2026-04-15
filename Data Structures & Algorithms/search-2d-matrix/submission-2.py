class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) * len(matrix[0])-1

        while l <= r:
            print(l,r)
            m = l + ((r-l) // 2)
            row, col = m // len(matrix[0]), m % len(matrix[0])
            print(m, row, col)
            if matrix[row][col] > target:
                r -= 1
            elif matrix[row][col] < target:
                l += 1
            else:
                return True


        return False