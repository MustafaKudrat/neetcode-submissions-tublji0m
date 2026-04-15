class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        pos = 0
        for i in range(0,len(strs)):
            cur = strs[i]
            res += cur
            res += ";"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        cur = ""
        for i in range(0,len(s)):
            if s[i] == ";":
                res.append(cur)
                cur = ""
            else:
                cur += s[i]

        return res