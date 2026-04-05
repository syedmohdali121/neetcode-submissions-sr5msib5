"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals or len(intervals) == 1:
            return True

        intervals.sort(key = lambda x: x.start)

        attend_meet = False

        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                attend_meet = False
                break
            else:
                attend_meet = True

        return attend_meet
