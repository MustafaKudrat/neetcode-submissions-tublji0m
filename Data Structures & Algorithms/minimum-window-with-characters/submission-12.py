class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        tCounter = Counter(t)
        wCounter = defaultdict(int)
        need = len(tCounter)
        have = 0

        minL, minR = -1, len(s)
        l, r = 0, 0
        while r < len(s):
            wCounter[s[r]] += 1
            if s[r] in tCounter and wCounter[s[r]] == tCounter[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < (minR - minL + 1):
                    minL, minR = l, r
                wCounter[s[l]] -= 1
                if s[l] in tCounter and wCounter[s[l]] < tCounter[s[l]]:
                    have -= 1
                l += 1

            r += 1
        return s[minL: minR + 1] if minL != -1 else ""
        

