class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        i = 0
        res = 0
        while i < len(nums):
            if nums[i] - 1 in numSet:
                i += 1
                continue
            curLen = 1
            j = 1
            while nums[i] + j in numSet:
                curLen += 1
                j += 1
            res = max(res, curLen)
            i += 1

        return res
        