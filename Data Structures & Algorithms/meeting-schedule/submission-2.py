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
        intervals.sort(key= lambda x:x.start)
        booked_s,booked_e = intervals[0].start,intervals[0].end

        for interval in intervals[1:]:
            s,e = interval.start,interval.end
            if booked_s <=s<booked_e:
                return False
            else:
                booked_e = e
        
        return True
