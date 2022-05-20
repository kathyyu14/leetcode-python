"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {None:None}
        p = head
        
        while p:
            hashMap[p] = Node(p.val)
            p = p.next
        
        p = head
        
        while p:
            copy = hashMap[p]
            copy.next = hashMap[p.next]
            copy.random = hashMap[p.random]
            p = p.next
        
        return hashMap[head]
    
 