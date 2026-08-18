"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key= lambda x:x.end)
        lastEnd = intervals[0].end

        for elem in intervals[1:]:
            start, end = elem.start, elem.end
            if start < lastEnd:
                return False
            else:
                lastEnd = end
        
        return True



        
