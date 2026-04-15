class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for st in strs:
            res.append(str(len(st)) + '#' + st)
        return "".join(res)



    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i: j])
            i = j + 1
            j = i + length
            res.append(s[i: j])
            i = j
        return res


#    def encode(self, strs: List[str]) -> str:
#        res = ""
#        pos = 0
#        for i in range(0,len(strs)):
#            cur = strs[i]
#            res += cur
#            res += ";"
#
#        return res
#
#    def decode(self, s: str) -> List[str]:
#        res = []
#        cur = ""
#        for i in range(0,len(s)):
#            if s[i] == ";":
#                res.append(cur)
#                cur = ""
#            else:
#                cur += s[i]
#        return res
