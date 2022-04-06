#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in hashMap.keys():
                return [hashMap[num], i]
            
            hashMap[nums[i]] = i


        '''
        hash map

        One-pass Hash Table

        Time complexity: O(n)

        Space complexity: O(n)
        '''
# @lc code=end

