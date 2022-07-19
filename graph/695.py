class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # initializing
        rows = len(grid)
        cols = len(grid[0])
        visited = set() # hash map
        
        # dfs defination
        # edge cases -> mark visited -> recursively dfs
        def dfs(row, col):
            if(row < 0 or row == rows or col < 0 or col == cols or grid[row][col] == 0 or (row, col) in visited): # row, col不出界，该点不是小岛, 该点已经被visited
                return 0
            visited.add((row, col))
            return (1 + dfs(row + 1, col) +
                        dfs(row - 1, col) +
                        dfs(row, col + 1) +
                        dfs(row, col - 1))
        
        # traverse all the point of the graph, record max area
        area = 0
        for row in range(rows):
            for col in range(cols):
                area = max(area, dfs(row, col))
        return area