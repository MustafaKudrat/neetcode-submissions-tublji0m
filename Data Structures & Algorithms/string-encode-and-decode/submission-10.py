class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)) + '#' + s)
        
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            start = i
            while s[i] != '#':
                i += 1
            print(start, i)
            size = int(s[start:i])
            res.append(s[i + 1: i + 1 + size])
            i = i + 1 + size
        
        return res

