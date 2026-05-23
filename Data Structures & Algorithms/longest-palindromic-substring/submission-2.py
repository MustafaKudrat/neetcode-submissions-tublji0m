class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        resL, resR = 0, 0
        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    resL, resR = l, r
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    resL, resR = l, r
                l -= 1
                r += 1

        return s[resL: resR + 1]


