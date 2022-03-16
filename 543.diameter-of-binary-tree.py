#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiamiter = [0]
        def maxDepth(node):
            if not node:
                return 0
            
            leftMax = maxDepth(node.left)
            rightMax = maxDepth(node.right)
            maxDiamiter[0] = max(maxDiamiter[0], leftMax + rightMax)
            
            return 1 + max(leftMax, rightMax)
        
        maxDepth(root)
        return maxDiamiter[0]
        
# @lc code=end

