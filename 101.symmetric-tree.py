#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        resLeft=[]
        resRight=[]
        def leftInorder(root):
            if root is None:
                resLeft.append(None)
                return
            resLeft.append(root.val)
            leftInorder(root.left)
            leftInorder(root.right)
        
        def rightInorder(root):
            if root is None:
                resRight.append(None)
                return
            resRight.append(root.val)
            rightInorder(root.right)
            rightInorder(root.left)
        
        leftInorder(root)
        rightInorder(root)
        
        if resLeft == resRight:
            return True
        
        return False
        
# @lc code=end

