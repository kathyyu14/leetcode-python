# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        res = []
        
        if not root:
            return res
        
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                level.append(curr.val)
            res.append(level[-1])
        
        return res