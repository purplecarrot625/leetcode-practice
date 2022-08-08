# 226 Invert Binary tree
### DFS Method
注意不要忘记判断root是否为空，每次递归的点相当于root
- 判断root是否为空
- 交换左右孩子
- 递归调用，左子树；递归调用，右子树

``` python
if not root:
    return None
temp = root.left
root.left = root.right
root.right = temp
        
self.invertTree(root.left)
self.invertTree(root.right)
        
return root
        
```
### BFS Method

- init deque: q = deque([root])
- while q: if has left/right child, append!
- level + 1

``` python
# bfs
        if not root: 
            return 0
        q = deque([root])
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
```

# 102 BFS 模板

``` python
q = deque()

while q:
    val = []
    for i in range(len(q)):
        node = q.popleft()
        val.append(node.val)

        if node.left:
            q.append(node.left)
        if node.right:
            q.appenf(node.right)
    res.append(val)
    
return res
```

# 199. Binary Tree Right Side View
 用bfs
 rightSide保存了这一层最后一个遍历到达节点

``` python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])
        
        while q:
            rightSide = None
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
```

# 1448. Count Good Nodes in Binary Tree
*Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.*

## dfs 模板
实时记录每条路中的最大值，用dfs遍历，如果是good:也就是说node的值大于当前最大值,则result+1,即return 1, 相反return 0
``` python
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0
        
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        return dfs(root, root.val)
  ```                      


  # 105. Construct Binary Tree from Preorder and Inorder Traversal

  ``` python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if not preorder or not inorder:
            return None
        
        #根结点是前序遍历的第一个点
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        
        midIndex = inorder.index(rootVal) # 根结点的值找元素下标
        
        # 中序遍历左子树：【0，midindex】，右子树：【midindex+1，n-1】
        inorderLeft = inorder[:midIndex]
        inorderRight = inorder[midIndex + 1:]
        
        # 前序遍历和中序遍历左右子树长度相等
        preorderLeft = preorder[1:len(inorderLeft) + 1]
        preorderRight = preorder[len(inorderLeft) + 1:]
        
        # 递归遍历左右子树
        root.left = self.buildTree(preorderLeft, inorderLeft)
        root.right = self.buildTree(preorderRight, inorderRight)
        
        return root
  ```

# 98. Validate Binary Search Tree
  ```python
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
  ```