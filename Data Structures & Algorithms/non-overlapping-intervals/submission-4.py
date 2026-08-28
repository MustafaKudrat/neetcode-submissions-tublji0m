class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
       
        for interval in intervals[1:]:
            if interval[0] < prevEnd:
                res += 1
                prevEnd = min(interval[1], prevEnd)
            else:
                prevEnd = interval[1]

        return res