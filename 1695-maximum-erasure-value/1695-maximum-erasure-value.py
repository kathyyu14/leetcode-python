class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        res, total = 0, 0
        visited = set()
        
        for r in range(len(nums)):
            while nums[r] in visited:
                visited.remove(nums[l])
                total -= nums[l]
                l += 1
            
            visited.add(nums[r])
            total += nums[r]
            res = max(res, total)
            
        return res