class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#         hashmap = {}
#         for num in nums:
#             if num not in hashmap:
#                 hashmap[num] = 1
#             hashmap[num] += 1
        
        
#         maxNum = 0
#         res = 0
        
#         for idx, value in hashmap.items():
#             if value > maxNum:
#                 res = idx
#                 maxNum = value
        
#         return res
        
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)