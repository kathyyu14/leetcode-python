class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right
        
        while left <= right:
            totalHour = 0
            mid = (right+left)//2
            
            for pile in piles:
                totalHour += math.ceil(pile / mid)
            
            if totalHour <= h:
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        
        return res