class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sRes = {}
        tRes = {}

        for ch in s:
            sRes[ch] = sRes.get(ch, 0) + 1
        for c in t:
            tRes[c] = tRes.get(c, 0) + 1
        
        if sRes != tRes:
            return False
        
        return True