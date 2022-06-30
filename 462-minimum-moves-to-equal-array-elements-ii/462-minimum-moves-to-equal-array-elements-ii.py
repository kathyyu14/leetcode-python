class Solution:
    def minMoves2(self, nums: List[int]) -> int:
#         res = float('inf')
        
#         for n in nums:
#             total = 0
#             for num in nums:
#                 total += abs(n - num)
#             res = min(res, total)
        
#         return res
        nums.sort()
        res = 0
        medium = nums[len(nums) // 2]
        for n in nums:
            res += abs(medium - n)
        
        return res
        
        