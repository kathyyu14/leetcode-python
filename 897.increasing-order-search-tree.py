#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        tree = TreeNode(None)
        def bstInorder(root):
            if not root:
                return None
            
            bstInorder(root.left)
            res.append(root.val)
            bstInorder(root.right)
               
        bstInorder(root)
        for v in res:
            tree.right = TreeNode(v)
            tree = tree.right
            
        return tree  
# @lc code=end

