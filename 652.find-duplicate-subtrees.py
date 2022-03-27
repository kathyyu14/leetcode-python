#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from typing import Collection, Counter

class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        counts = collections.Counter()
        res = []

        def dfs(root):
            if not root:
                return ''
            
            left = dfs(root.left)
            right = dfs(root.right)

            subTree = str(root.val) + ',' + left + ',' + right

            counts[subTree] += 1

            if counts[subTree] == 2:
                res.append(root)

            return subTree
        print(counts)
        dfs(root)
        return res



# @lc code=end

