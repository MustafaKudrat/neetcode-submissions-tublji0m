class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # A B C D B X Y Z R T
        # 1 2 3 4 5
        # A    
        res = 0
        mp = {}    
        l = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)

        return res