class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        tCounter = Counter(t)
        wCounter = defaultdict(int)
        need = len(tCounter)
        have = 0

        minL, minR = -1, len(s)
        l = 0
        for r in range(len(s)):
            wCounter[s[r]] += 1
            if s[r] in tCounter and wCounter[s[r]] == tCounter[s[r]]:
                have += 1
            while have == need:
                if r - l < minR - minL:
                    minR, minL = r, l
                wCounter[s[l]] -= 1
                if s[l] in tCounter and wCounter[s[l]] < tCounter[s[l]]:
                    have -= 1
                l += 1
        return s[minL: minR + 1] if minL != -1 else ""
                