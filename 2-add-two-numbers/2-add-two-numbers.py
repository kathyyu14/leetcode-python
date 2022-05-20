# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        res,carry = [], 0
        p1 = l1
        p2 = l2
        dummy = ListNode(-1)
        p = dummy
        
        while p1 or p2:
            if p1 and p2:
                total = p1.val + p2.val + carry
            elif not p1:
                total = p2.val + carry
            else:
                total = p1.val + carry
            p.next = ListNode(total % 10)
            carry = total // 10
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            p = p.next
        if carry:
            p.next = ListNode(carry)
        
        return dummy.next
            
                
        