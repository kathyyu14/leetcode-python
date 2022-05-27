class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
#         heapify(nums)
        
#         while len(nums) > k:
#             heapq.heappop(nums)
        
#         return nums[0]
        k = len(nums) - k
        
        def quicksort(l,r):
            if l == r: return nums[l]
            
            pivot = nums[r]
            p = l
            
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p],nums[r] = nums[r], nums[p]
            
            if p > k : return quicksort(l, p - 1)
            elif p < k: return quicksort(p+1, r)
            else: return nums[p]
            
        
        return quicksort(0, len(nums)-1)
    

        
        