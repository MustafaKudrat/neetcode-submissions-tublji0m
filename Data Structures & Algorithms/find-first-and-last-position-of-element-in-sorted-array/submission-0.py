class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerBound(num, targ):
            l, r = 0, len(num)
            while l < r:
                mid = (l + r) // 2
                if num[mid] < targ:
                    l = mid + 1
                else:
                    r = mid

            return l

        def upperBound(num, targ):
            l, r = 0, len(num)
            while l < r:
                mid = (l + r) // 2
                if num[mid] <= targ:
                    l = mid + 1
                else:
                    r = mid

            return l

        first, last = lowerBound(nums, target), upperBound(nums, target) - 1
        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        else:
            return [first, last]