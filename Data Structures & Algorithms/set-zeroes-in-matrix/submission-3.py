class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # traverse the matrix and use first row and col as flags
            # topLeft for first row flag
        topLeft = False
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        topLeft = True

        # update all inner cells
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # update first col
        if matrix[0][0] == 0:
            for r in range(len(matrix)):
                matrix[r][0] = 0

        # update first row with topLeft flag
        if topLeft:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0

        
        