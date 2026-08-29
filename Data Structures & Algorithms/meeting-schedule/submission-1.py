"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        L, R = 0, 1
        intervals = sorted(intervals, key=lambda x: x.end)
        while R < len(intervals):
            if intervals[L].end > intervals[R].start:
                return False
            L += 1
            R += 1
        return True