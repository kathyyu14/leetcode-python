#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = [root]

        if not root: 
            return res

        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.pop(0)
                level.append(curr.val)
    
                if curr.left is not None:
                    queue.append(curr.left)

                if curr.right is not None:
                    queue.append(curr.right)

            res.append(level)
        
        return res
        
# @lc code=end
