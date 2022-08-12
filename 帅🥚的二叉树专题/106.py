# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Treminal case: empty tree
        if not inorder or not postorder:
            return None
        
            
        # The last element of postorder is root!
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        
        # Find midIndex with root value in inorder
        midIndex = inorder.index(rootVal)
        
        # Find the left and right of inorder
        inorderLeft = inorder[:midIndex]
        inorderRight = inorder[midIndex + 1:]
        
        # Find the left and right of postorder
        postorderLeft = postorder[: len(inorderLeft)]
        postorderRight = postorder[len(inorderLeft): len(inorder) - 1] # 注意这里

        
        # Build left subtree
        root.left = self.buildTree(inorderLeft, postorderLeft)
        
        # Build right subtree
        root.right = self.buildTree(inorderRight, postorderRight)
        
        return root