#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.



# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
可以用前序遍历和后续遍历以及层次遍历来解决问题
但是不能用中序遍历

首先要构造 root 节点。前序遍历得到的 nodes 列表中，第一个元素是 root 节点的值；后序遍历得到的 nodes 列表中，最后一个元素是 root 节点的值。

你看上面这段中序遍历的代码，root 的值被夹在两棵子树的中间，也就是在 nodes 列表的中间，我们不知道确切的索引位置，所以无法找到 root 节点，也就无法进行反序列化。

'''

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node):
            if not node:
                res.append('#')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(',')

        def dfs():
            val = vals.pop(0)
            if val == '#':
                return
                
            root = TreeNode(int(val))
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()

        # def rdeserialize(l):
        #     """ a recursive helper function for deserialization."""
        #     if l[0] == '#':
        #         l.pop(0)
        #         return None
                
        #     root = TreeNode(l[0])
        #     l.pop(0)
        #     root.left = rdeserialize(l)
        #     root.right = rdeserialize(l)
        #     return root

        # data_list = data.split(',')
        # root = rdeserialize(data_list)
        # return root

            


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

