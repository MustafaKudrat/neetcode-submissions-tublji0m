class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        row = [1]
        for i in range(1, numRows + 1):
            res.append(row)
            row = [1] + [row[j] + row[j+1] for j in range(len(row) - 1)] +[1]
        return res
