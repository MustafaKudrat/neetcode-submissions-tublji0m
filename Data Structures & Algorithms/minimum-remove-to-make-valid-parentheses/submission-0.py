class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        traverse the s and get the cnt for inbalance
            remove extra )
        reverse the s and remove extra ( from the back
        return the reversed join
        '''
        
        '''
        ab(c)(
        cnt = 1
        
        '''

        cnt = 0
        st = list(s)
        for i, ch in enumerate(st):
            if ch == "(":
                cnt += 1
            elif ch == ")" and cnt > 0:
                cnt -= 1
            elif ch == ")":
                st[i] = ""
        
        res = []

        for ch in reversed(st):
            if ch == "(" and cnt > 0:
                cnt -= 1
            else:
                res.append(ch)

        return "".join(reversed(res))

