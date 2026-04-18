class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2,20,4,10,3,5
        maxLen = 0
        numsSet = set(nums)
        for num in numsSet:
            if num - 1 not in numsSet:
                curLen = 1
                right = num + 1
                while right in numsSet:
                    curLen += 1
                    right += 1
                maxLen = max(maxLen, curLen)
        return maxLen
