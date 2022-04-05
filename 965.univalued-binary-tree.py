#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        #dfs: 再利用set的特性
        res = []
        
        def dfs(root):
            if not root:
                return None
            
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)
        return len(set(res)) == 1
# @lc code=end

