class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        
        prev = None
        res = ""
        
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            cnt, char = heapq.heappop(maxHeap) # pop the most freq item
            res += char
            cnt += 1
            
            if prev:
                heapq.heappush(maxHeap, prev) 
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
            
        
        return res