class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True
        
        ROWS, COLS = len(board), len(board[0])
        res = set()
        visited = set()

        def dfs(r, c, curNode, word):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or
                (r, c) in visited or
                board[r][c] not in curNode.children
            ):
                return
            
            visited.add((r, c))
            curNode = curNode.children[board[r][c]]
            word += board[r][c]
            if curNode.endOfWord:
                res.add(word)
            
            dfs(r + 1, c, curNode, word)
            dfs(r - 1, c, curNode, word)
            dfs(r, c + 1, curNode, word)
            dfs(r, c - 1, curNode, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(res)

        