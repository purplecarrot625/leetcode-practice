# 200. Number of Islands

### BFS

- 用islands来存岛屿的数量
- 用q来表示队列
- 用visited（set）来存哪些点被visit过

``` python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # to see if the grid exists
        if not grid:
            return 0
        visited = set()
        islands = 0
        
         # implement bfs
        def bfs(r, c):
            q = deque()
            visited.add((r, c))
            q.append((r, c))
            directions = [[-1,0], [1,0], [0,-1], [0,1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    
                    if (r,c) not in visited and r in range(len(grid)) and c in range(len(grid[0])) and grid[r][c] == '1':
                        q.append((r,c))
                        visited.add((r,c))
        
        # for each node in grid, if not visited, do bfs
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1 # mark the island, and explore all its ajascent nodes by using bfs search
                  
        return islands
    
       

```

# 133.Clone Graph

- Use hashMap to see if we have already added(copy) the node 用hashmap来储存哪些node已经被复制过了
- If the node is not in the hashMap, we copy it and add all it's neighbors recursively(dfs),(treat each neighbor as 'node', to find its neighbors...) 如果这个节点没有被复制过，那么加入这个节点，然后对待他所有的邻居像对待他一样，recursively！

``` python
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldToNew = {}
        
        def dfs_clone(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs_clone(nei))
            return copy
        
        return dfs_clone(node) if node else None
            

```