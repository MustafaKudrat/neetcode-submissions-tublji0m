class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            curArea = min(heights[r], heights[l]) * (r - l)
            res = max(res, curArea)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res