class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2,20,4,10,3,5
        if len(nums) == 0:
            return 0
        numsSet = set(nums)
        curLen = 1
        maxLen = 1
        for num in numsSet:
            right = num + 1
            if num - 1 in numsSet:
                curLen = 1
                continue
            while right in numsSet:
                curLen += 1
                maxLen = max(maxLen, curLen)
                right += 1
        return maxLen