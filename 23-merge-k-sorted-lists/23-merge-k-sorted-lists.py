# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        dummy = ListNode(-1)
        p = dummy
        
        for head in lists:
            while head:
                heapq.heappush(heap, head.val)
                head = head.next
        
        while heap:
            node = ListNode(heapq.heappop(heap))
            p.next = node
            p = p.next
        
        return dummy.next
        
        
        
        
        