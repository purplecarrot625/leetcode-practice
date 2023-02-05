# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preSum = 0
    
    def nodeSum(self, root):
        if root == None:
            return None
        # traverse right child
        self.nodeSum(root.right)
        root.val += self.preSum
        self.preSum = root.val
        self.nodeSum(root.left)
        
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.nodeSum(root)
        return root
        