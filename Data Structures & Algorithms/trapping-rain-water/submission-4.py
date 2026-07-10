class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        maxLeft = maxRight = 0
        l, r = 0, len(height) - 1
        while l < r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            res += min(maxLeft, maxRight) - min(height[l], height[r])
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return res