class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        tCounter = Counter(t)
        wCounter = defaultdict(int)

        l = 0
        have, need = 0, len(tCounter)
        resL, resR = -1, len(s)

        for r in range(len(s)):
            wCounter[s[r]] += 1
            if s[r] in tCounter and wCounter[s[r]] == tCounter[s[r]]:
                have += 1
            while have == need:
                if r - l < resR - resL:
                    resR, resL = r, l
                wCounter[s[l]] -= 1
                if s[l] in tCounter and wCounter[s[l]] < tCounter[s[l]]:
                    have -= 1
                
                l += 1
        return s[resL: resR + 1] if resL != -1 else ""