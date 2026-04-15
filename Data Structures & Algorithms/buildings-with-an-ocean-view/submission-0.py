class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        maxR = float('-inf')
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > maxR:
                res.append(i)
                maxR = heights[i]

        
        return res[::-1]
