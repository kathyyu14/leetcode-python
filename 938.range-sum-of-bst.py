#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = []
        def helper(root):
            if not root:
                return
            
            if root.val >= low and root.val <= high:
                res.append(root.val)
            
            helper(root.left)     
            helper(root.right)
            
        helper(root)
        return sum(res)
  
        '''
            BST 思路：
            可以利用BST的特性来解决问题
            如果都 > root.val 就在右子树
            如果都 < root.val 就是在左子树
            在区间内就加上
        ''' 
# @lc code=end

