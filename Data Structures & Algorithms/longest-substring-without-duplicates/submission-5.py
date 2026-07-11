class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 1
        if len(s) <= 1:
            return len(s)
        l, r = 0, 1
        window = set()
        window.add(s[l])
        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                res = max(res, r - l + 1)
                r += 1
            else:
                window.remove(s[l])
                l += 1
                #window.add(s[r])
        return res
