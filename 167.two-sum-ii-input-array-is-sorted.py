#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # hash map
        '''
        hashMap = {}
        for i in range(len(numbers)):
            key = target - numbers[i]
            if numbers[i] in hashMap.keys():
                return [hashMap[numbers[i]]+1, i+1]
            hashMap[key] = i
        '''

        # 2 point : binary search

        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else: 
                l += 1
        
# @lc code=end

