class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic non decreasing stack
        #   0, 7
        # 1, 6
        # 2, 7
        # 3, 2
        stack = []
        res = 0
        for i, h in enumerate(heights):
            idx = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                res = max(res, (i - idx) * height)
            stack.append((idx, h))
        
        while stack:
            idx, h = stack.pop()
            res = max(res, (len(heights) - idx) * h)
        
        return res

        