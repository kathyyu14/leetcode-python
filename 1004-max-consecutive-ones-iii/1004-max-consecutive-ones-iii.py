class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right, maxOnes, res = 0, 0, 0, 0
        
        while right < len(nums):
            if nums[right] == 1:
                maxOnes += 1
            right += 1
            
            while right - left - maxOnes > k:
                if nums[left] == 1:
                    maxOnes -= 1
                left += 1
            
            res = max(res, right - left)
        
        return res
                    