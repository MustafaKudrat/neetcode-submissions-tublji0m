class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        l, r = 0, len(height) - 1
        maxLeft, maxRight = 0, 0

        res = 0 #[0] * len(height)

        while l < r:
            if min(maxLeft, maxRight) - height[l] >= 0:
                res += min(maxLeft, maxRight) - height[l]
            if min(maxLeft, maxRight) - height[r] >= 0:
                res += min(maxLeft, maxRight) - height[r]
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])

            if maxLeft <= maxRight:
                l += 1
            else:
                r -= 1
        
        return res

