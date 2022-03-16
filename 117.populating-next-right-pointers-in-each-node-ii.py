#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        if root.left and root.right:
            root.left.next = root.right
        if root.left or root.right:
            if root.left:
                root.right.next = root.right.left
            else:
                root.right.next = root.right.right
        self.connect(root.left)
        self.connect(root.right)
        return root
        
# @lc code=end

