class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curList = []

        def bt(openP, closeP):
            if openP == closeP == n:
                res.append("".join(curList[:]))
                return
            
            if openP < n:
                curList.append("(")
                bt(openP + 1, closeP)
                curList.pop()
            
            if closeP < openP:
                curList.append(")")
                bt(openP, closeP + 1)
                curList.pop()
            
        bt(0, 0)
        return res