"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        counter, maxCounter = 0, 0
        L, R = 0, 0
        start, end = [], []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start = sorted(start)
        end = sorted(end)
        while L < len(start):
            if start[L] < end[R]:
                counter += 1
                L += 1
            else:
                counter -= 1
                R += 1
            maxCounter = max(maxCounter, counter)
        return maxCounter