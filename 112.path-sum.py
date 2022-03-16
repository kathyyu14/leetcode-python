#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
from pickle import FALSE
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node:
                return False
            currSum += node.val
            if not node.left and not node.right:
                return targetSum == currSum
            return dfs(node.left, currSum) or dfs(node.right, currSum)
        return dfs(root, 0)
# @lc code=end
