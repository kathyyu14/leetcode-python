class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        minNum = nums[0]
        
        while left <= right:
            if nums[left] < nums[right]:
                minNum = min(minNum, nums[left])
                break
            mid = left + (right-left) //2
            
            if nums[left] <= nums[mid]:
                minNum = min(nums[left], minNum)
                left = mid + 1
            else:
                if nums[mid] < nums[right]:
                    minNum = min(nums[mid], minNum)
                    right = mid - 1
                else:
                    left = mid + 1
                
            
        return minNum
            