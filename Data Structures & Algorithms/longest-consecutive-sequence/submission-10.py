class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 1 if len(nums) > 0 else 0

        for num in nums:
            curLen = 1
            if (num - 1) in numSet:
                continue
            j = 1
            while (num + j) in numSet:
                curLen += 1
                j += 1
            res = max(res, curLen)
        
        return res