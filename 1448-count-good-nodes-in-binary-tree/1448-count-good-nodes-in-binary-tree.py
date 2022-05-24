# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        
        def traverse(node, pathmax):
            if not node:
                return 
            
            if node.val >= pathmax:
                self.count += 1
                
            pathmax = max(node.val, pathmax)
                
            traverse(node.left, pathmax)
            traverse(node.right, pathmax)
        
        traverse(root, root.val)
        return self.count