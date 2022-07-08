class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        
        def searchPair(target, left):
          number = 0
          l, r = left + 1, len(nums) - 1
          while l < r:
            if nums[l] + nums[r] < target:
              number += r - l
              l += 1
            else:
              r -= 1
          return number
        
        for i in range(len(nums) - 2):
          count += searchPair(target - nums[i], i)
        
        return count