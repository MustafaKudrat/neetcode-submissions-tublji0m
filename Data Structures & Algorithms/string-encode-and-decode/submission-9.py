class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for st in strs:
            res += str(len(st)) + '#' + st
        
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            size = ''
            while s[i].isdigit():
                size += s[i]
                i += 1
            res.append(s[i + 1: i + int(size) + 1])
            i += int(size) + 1
        return res
            