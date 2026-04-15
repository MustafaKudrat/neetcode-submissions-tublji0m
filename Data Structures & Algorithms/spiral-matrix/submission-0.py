class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []

        while l < r and top < bottom:
            # go thru top
            for i in range(l, r):
                res.append(matrix[top][i])
            top += 1


            #go thru right 
            for i in range(top, bottom):
                res.append(matrix[i][r-1])
            r -= 1
            
            #check boundry
            if l >= r or top >= bottom:
                break

            # bottom
            for i in range(r-1, l-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            # left
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][l])
            l += 1


        return res