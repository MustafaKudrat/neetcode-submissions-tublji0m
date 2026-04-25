class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if target in range(nums[l], nums[m] + 1):
                    r = m
                else:
                    l = m + 1
            else:
                if target in range(nums[m], nums[r] + 1):
                    l = m
                else:
                    r = m - 1
        return -1
        