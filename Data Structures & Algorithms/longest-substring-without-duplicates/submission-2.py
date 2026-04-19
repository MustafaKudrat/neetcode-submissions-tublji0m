class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # A B C D B X Y Z R T
        # 1 2 3 4 5
        # A    
        res = 0
        curSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in curSet:
                curSet.remove(s[l])
                l += 1
            curSet.add(s[r])
            res = max(res, r - l + 1)

        return res