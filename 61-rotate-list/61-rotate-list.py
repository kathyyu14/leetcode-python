# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
          return head
        
        # Iterate to the list tail and get list size
        curr = head
        size = 1
        while curr.next:
          curr = curr.next
          size += 1
        
        # Compute the actual number that need to be rotated
        k %= size
        if k == 0:
          return head
        
        # connect the tail and head
        curr.next = head
        
        curr = head
        for _ in range(size - k - 1):
          curr = curr.next
        
        newHead = curr.next
        curr.next = None
        
        return newHead
        
        