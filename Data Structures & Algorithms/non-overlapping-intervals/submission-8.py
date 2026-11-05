class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res=0
        intervals.sort(key=lambda x: x[1])
        prevend=intervals[0][1]
        for start, end in intervals[1:]:
            if start<prevend:
                res+=1    
            else:
                prevend=end
        return res

        