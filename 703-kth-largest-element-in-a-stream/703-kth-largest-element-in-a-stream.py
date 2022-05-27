class KthLargest:
    from heapq import heappush, heappop

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []
        for num in nums:
            heappush(self.h, num)
            if len(self.h) > k:
                heappop(self.h)
        

    def add(self, val: int) -> int:
        heappush(self.h, val)
        if len(self.h) > self.k:
            heappop(self.h)
        return self.h[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)