class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x:x[0])
        end = float("-inf")
        
        for s, e in intervals:
            if s < end:
                return False
            end = e
        
        return True
        