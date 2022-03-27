#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(root, min, max):
            if not root:
                return True
            
            if min and root.val <= min.val:
                return False
            
            if max and root.val >= max.val:
                return False

            return isValid(root.left, min, root) and isValid(root.right, root, max)
        
        return isValid(root, None, None)
# @lc code=end

