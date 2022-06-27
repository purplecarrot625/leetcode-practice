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
    
       