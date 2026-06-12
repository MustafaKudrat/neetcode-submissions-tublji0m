class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        maxLen = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in res:
                res.add(s[r])
                maxLen = max(maxLen, r - l + 1)
                r += 1
            else:
                while l < r and s[r] in res:
                    res.remove(s[l])
                    l += 1 
        return maxLen