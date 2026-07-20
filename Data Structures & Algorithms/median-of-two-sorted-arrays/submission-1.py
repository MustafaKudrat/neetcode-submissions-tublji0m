class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1 4 5 6 6
        # 2 4 6 9
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        l, r = 0, len(nums1) - 1
        while True:
            m1 = (l + r) // 2
            m2 = half - m1 - 2

            nums1left = nums1[m1] if m1 >= 0 else float('-inf')
            nums1right = nums1[m1 + 1] if m1 + 1 < len(nums1) else float('inf')

            nums2left = nums2[m2] if m2 >= 0 else float('-inf')
            nums2right = nums2[m2 + 1] if m2 + 1 < len(nums2) else float('inf')

            if nums1left <= nums2right and nums2left <= nums1right:
                if total % 2 == 0:
                    return (max(nums1left, nums2left) + min(nums1right, nums2right)) / 2
                else:
                    return min(nums1right, nums2right)
            elif nums1left > nums2right:
                r = m1 - 1
            else:
                l = m1 + 1