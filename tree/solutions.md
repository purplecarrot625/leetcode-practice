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

