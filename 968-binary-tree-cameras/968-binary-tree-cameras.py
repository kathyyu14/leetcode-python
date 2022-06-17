# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node):
            if not node: return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == 1 or right == 1:
                self.res += 1
                return 2
            if left == 2 or right == 2:
                return -1
            if node != root:
                return 1
            self.res += 1
        
        dfs(root)
        return self.res