class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCount = Counter(t)
        l = 0
        wCount = defaultdict(int)
        res = ""
        maxLen = len(s)
        need, have = len(tCount), 0
        for r in range(len(s)):
            wCount[s[r]] += 1
            if wCount[s[r]] == tCount[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) <= maxLen:
                    maxLen = r - l + 1
                    res = s[l:r + 1]
                
                wCount[s[l]] -= 1
                if s[l] in tCount and wCount[s[l]] < tCount[s[l]]:
                    have -= 1
                l += 1
        return res