# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # put listnode into stack to get the backward
        stack = []
        p = head
        
        while p:
            stack.append(p)
            p = p.next
        
        p = head
        while p:
            lastNode = stack.pop()
            nxt = p.next
            if lastNode == nxt or lastNode.next == nxt:
                lastNode.next = None
                break
                
            p.next = lastNode
            lastNode.next = nxt
            p = nxt
        
        return p