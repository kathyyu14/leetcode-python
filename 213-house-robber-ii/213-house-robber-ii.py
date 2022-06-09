class Solution:
    def rob(self, nums: List[int]) -> int:
        maxRob = 0
        
        def dp(nums):
            rob1, rob2 = 0, 0
            
            for num in nums:
                tmp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = tmp
            
            return max(rob1,rob2)
        
        res = max(nums[0], dp(nums[1:]), dp(nums[:-1]))
        return res
                