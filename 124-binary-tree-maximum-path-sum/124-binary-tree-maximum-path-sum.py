# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = float('-inf')
        
        if not root:
            return 0
        
        def sideMaxPath(root):
            if not root:
                return 0
            
            left = max(0, sideMaxPath(root.left))
            right = max(0, sideMaxPath(root.right))
            self.maxPath = max(self.maxPath, left+right+root.val)
            
            return root.val + max(left,right)
        
        sideMaxPath(root)
        return self.maxPath