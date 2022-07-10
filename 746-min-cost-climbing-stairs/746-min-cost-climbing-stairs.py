class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1 = cost[0]
        dp2 = cost[1]
        
        for i in range(2, len(cost)):
          dp = min(dp2, dp1)  + cost[i]
          dp1 = dp2
          dp2 = dp
        
        return min(dp1, dp2)