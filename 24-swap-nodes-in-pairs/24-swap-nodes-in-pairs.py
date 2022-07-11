# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
          return head
        
        dummy = p = ListNode(-1)
        dummy.next = head
        
        while head and head.next:
          tmp = head.next
          head.next = tmp.next
          tmp.next = head
          p.next = tmp
          head = head.next
          p = tmp.next
        
        return dummy.next

