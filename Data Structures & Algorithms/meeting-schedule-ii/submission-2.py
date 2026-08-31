"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        L, R = 0, 0
        currCount, maxCount = 0, -1
        sortedStarts = []
        sortedEnds = []
        for i in intervals:
            sortedStarts.append(i.start)
            sortedEnds.append(i.end)
        sortedStarts = sorted(sortedStarts)
        sortedEnds = sorted(sortedEnds)
        while L < len(intervals):
            if sortedStarts[L] < sortedEnds[R]:
                currCount += 1
                L += 1
            else:
                currCount -= 1
                R += 1
            maxCount = max(currCount, maxCount)
        return maxCount if maxCount > 0 else 0
        