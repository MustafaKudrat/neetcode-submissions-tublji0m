class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < nums[r]:
                if target not in range(nums[m], nums[r] + 1):
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target not in range(nums[l], nums[m] + 1):
                    l = m + 1
                else:
                    r = m - 1
        return -1