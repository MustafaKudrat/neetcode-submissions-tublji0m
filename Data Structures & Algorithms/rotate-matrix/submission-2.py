class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top = l
                bottom = r

                #save top left
                topLeft = matrix[top][top + i]

                #assign top left
                matrix[top][top + i] = matrix[bottom - i][top]

                #assign bottom left
                matrix[bottom - i][top] = matrix[bottom][bottom - i]

                #assign bottom right
                matrix[bottom][bottom - i] = matrix[top + i][bottom]

                #assign top right
                matrix[top + i][bottom] = topLeft

            l += 1
            r -= 1
        