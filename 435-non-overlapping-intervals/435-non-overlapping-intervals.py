class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, count = float('-inf'), 0
        
        intervals = sorted(intervals, key = lambda x: x[1])

        for s,e in intervals:
            if s >= end:
                end = e
            else:
                count += 1
        
        return count