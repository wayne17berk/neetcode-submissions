"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # intervals.sort()
        # prevend=intervals[0][1]
        # for start, end in intervals:
        #     if start<prevend:
        #         prevend=end
        #     else:
        #         return False
        # return True

        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i-1].end >intervals[i].start:  
                return False
        return True