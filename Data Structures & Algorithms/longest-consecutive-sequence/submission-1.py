class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        curLen = 1
        maxSize = 1
        curNum = nums[0]
        for num in nums[1:]:
            if num == curNum + 1:
                curLen += 1
                curNum = num
            elif num == curNum:
                continue
            else:
                curNum = num
                curLen = 1
            maxSize = max(curLen, maxSize)

        return maxSize