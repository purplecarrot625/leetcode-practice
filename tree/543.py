# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0] # global variable
        def dfs(root):
            if not root:
                return -1 # the height of a empty tree is -1
            
            left = dfs(root.left) #left subtree
            right = dfs(root.right) #right subtree
            res[0] = max(res[0], 2+left+right) # diameter, update the result
            
            return 1+max(left,right) # height, so we won't traverse each node every time
        dfs(root)
        return res[0]