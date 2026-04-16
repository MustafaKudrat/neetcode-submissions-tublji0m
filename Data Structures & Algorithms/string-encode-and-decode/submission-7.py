class Solution:
    # len(s) not always 0-9
    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st)) + ';' + st
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ';':
                j += 1
            size = int(s[i: j])
            start = j + 1
            end = start + size
            res.append(s[start: end])
            i = end
        return res