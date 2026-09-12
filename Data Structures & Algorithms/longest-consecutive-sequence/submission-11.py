class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in numSet:
                curLen = 1
                while num + curLen in numSet:
                    curLen += 1
                res = max(res, curLen)
        
        return res