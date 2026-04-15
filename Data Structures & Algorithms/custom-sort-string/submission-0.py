class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        res = ""

        for ch in order:
            if ch in count:
                for _ in range(count[ch]):
                    res += ch
                del count[ch]

        for ch in count:
            for _ in range(count[ch]):
                res += ch

        return res
        

        