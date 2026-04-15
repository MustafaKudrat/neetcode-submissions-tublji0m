"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = [i.start for i in intervals]
        end = [i.end for i in intervals]

        start.sort()
        end.sort()

        s = e = 0
        res = curRes = 0

  #start : 0,5,15
  #end : 10,20,40
        while s < len(start):
            if start[s] < end[e]:
                curRes += 1
                s += 1
            else:
                curRes -= 1
                e += 1
            
            res = max(res, curRes)
        return res



