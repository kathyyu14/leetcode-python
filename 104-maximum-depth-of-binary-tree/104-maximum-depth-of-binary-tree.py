# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # solution 1: 
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        #solution2:
                    
        self.res = 0
        self.depth = 0
        
        def dfs(root):
            if not root:
                return 0
            
            self.depth += 1
            if not root.left and not root.right:
                self.res = max(self.res, self.depth)
            dfs(root.left)
            dfs(root.right)
            self.depth -= 1
            
        dfs(root)
        return self.res
        
        
        
        
            