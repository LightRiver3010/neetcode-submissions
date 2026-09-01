"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        L, R = 0, 0
        maxRoom = 0
        countRoom = 0
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts = sorted(starts)
        ends = sorted(ends)
        while L < len(starts):
            if starts[L] < ends[R]:
                countRoom += 1
                L += 1
            else:
                countRoom -= 1
                R += 1
            maxRoom = max(countRoom, maxRoom)
        return maxRoom