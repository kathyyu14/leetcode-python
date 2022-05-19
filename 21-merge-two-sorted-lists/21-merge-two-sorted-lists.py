# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy

        p1 = l1
        p2 = l2
        
        while p1 and p2:
            if p1.val > p2.val:
                p.next = ListNode(p2.val)
                p2 = p2.next
            else:
                p.next = ListNode(p1.val)
                p1 = p1.next
            p = p.next
        
        if not p1:
            p.next = p2
        if not p2:
            p.next = p1
        
        return dummy.next