class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDup = set(nums)
        return len(noDup) != len(nums)