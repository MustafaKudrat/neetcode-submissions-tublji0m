class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x:x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            newStart = intervals[i][0]
            newEnd = intervals[i][1]
            end = res[-1][1]

            if newStart <= end:
                res[-1][1] = max(newEnd, end)
            else:
                res.append(intervals[i])


        return res