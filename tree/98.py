# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(node, left, right):
            # 空的树仍然是一个binary search tree
            if not node:
                return True
            
            # break the rules, return False
            if not (node.val < right and node.val > left):
                return False
            
            # 因为左孩子的value小于当前父值，所以右界更新为当前父值; 右孩子的value大于当前父值，所以左界更新为当前父值
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        return valid(root, float("-inf"), float("inf"))