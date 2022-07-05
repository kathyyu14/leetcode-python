class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        minHeap = []
        res = 0
        
        for interval in intervals:
          while len(minHeap) > 0 and interval[0] >= minHeap[0]:
            heapq.heappop(minHeap)
          heapq.heappush(minHeap, interval[1])
          res = max(res, len(minHeap))
          
        return res