class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            curSeq = 1
            cur = num
            while cur + 1 in numSet:
                cur += 1
                curSeq += 1
            res = max(res, curSeq)
        return res