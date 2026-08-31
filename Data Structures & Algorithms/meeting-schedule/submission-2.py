"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedArr = sorted(intervals, key=lambda x: x.end)
        for i in range(len(sortedArr)-1):
            if sortedArr[i].end > sortedArr[i+1].start:
                return False
        return True