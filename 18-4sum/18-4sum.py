class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def searchPair(first, second, res):
          l = second + 1
          r = len(nums) - 1
          
          while l < r:
            total = nums[l] + nums[r] + nums[first] + nums[second]
            if total == target:
              res.append([nums[first], nums[second], nums[l], nums[r]])
              l += 1
              r -= 1
              while l < r and nums[l] == nums[l - 1]:
                l += 1
              while l < r and nums[r] == nums[r + 1]:
                r -= 1
            elif total < target:
              l += 1
            else:
              r -= 1
        
        for i in range(len(nums) - 3):
          if i > 0 and nums[i] == nums[i - 1]:
            continue
          for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
              continue
            searchPair(i, j, res)
        
        return res