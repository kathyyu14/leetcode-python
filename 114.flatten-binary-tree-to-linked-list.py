#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
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
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # method1: 左边子树拼接在右边，遍历右边找到尾部并且拼接
        '''
         if not root:
            return None

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left

        p = root
        while p.right != None:
            p = p.right

        p.right = right
        '''

        # method2: 利用python 特性

        def dfs(node):
            if not node:
                return None
         
            leftTail = dfs(node.left)
            rightTail = dfs(node.right)

            if node.left:
                leftTail.right = node.right
                node.right = node.left
                node.left = None
          
            last = rightTail or leftTail or node
            
            return last

        dfs(root)


       
           
        
# @lc code=end

