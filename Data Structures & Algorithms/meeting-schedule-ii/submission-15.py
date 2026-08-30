"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([x.start for x in intervals])
        end = sorted([x.end for x in intervals])

        res = 0
        count = 0
        i, j = 0, 0

        while i < len(start):
            if start[i] < end[j]:
                count += 1
                res = max(res, count)
                i += 1
            else:
                j += 1
                count -= 1
        
        return res
