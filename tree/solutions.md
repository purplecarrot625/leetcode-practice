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