class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if len(nums) == 0: 
            return 0
        
        dp = {}
        
        def backtrack(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            
            if (i,total) in dp:
                return dp[(i,total)]
            
            dp[(i,total)] = (backtrack(i+1, total+nums[i]) + backtrack(i+1, total-nums[i]))
            
            return dp[(i,total)]
        
        return backtrack(0,0)