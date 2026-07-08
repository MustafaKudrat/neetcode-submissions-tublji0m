class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        sqrSet = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != '.':
                    s = ((r // 3), (c // 3))
                    if (board[r][c] in rowSet[r]
                    or board[r][c] in colSet[c]
                    or board[r][c] in sqrSet[s]):
                        return False

                    rowSet[r].add(board[r][c])
                    colSet[c].add(board[r][c])
                    sqrSet[s].add(board[r][c])
        
        return True