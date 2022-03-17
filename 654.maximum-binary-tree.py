#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from queue import Empty


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        maxNum = max(nums)
        index = nums.index(maxNum)
        root = TreeNode(maxNum)

        root.left = self.constructMaximumBinaryTree(nums[:index])
        root.right = self.constructMaximumBinaryTree(nums[index+1:])

        return root    
        

        
# @lc code=end

