class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))])
        
        minHeap = []
        maxProfit = 0
        curProfit = 0
        
        for s,e,p in jobs:
          while minHeap and minHeap[0][0] <= s:
            _, tmp = heapq.heappop(minHeap)
            curProfit = max(curProfit, tmp)
          
          heapq.heappush(minHeap, (e, curProfit + p))
          maxProfit = max(maxProfit, curProfit + p)
        
        return maxProfit