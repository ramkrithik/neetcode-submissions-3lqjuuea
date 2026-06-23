class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        while len(intervals):
            if len(intervals) == 1:
                result.append(intervals[0])
                intervals.pop()
                break
            if intervals[0][1] < intervals[1][0]:
                result.append(intervals[0])
                intervals.pop(0)
            else:
                new = [min(intervals[0][0],intervals[1][0]), max(intervals[0][1],intervals[1][1])]
                intervals.pop(0)
                intervals.pop(0)
                intervals.insert(0,new)
        
        return result
        