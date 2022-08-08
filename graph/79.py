class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # dfs
        row = len(board)
        col = len(board[0])
        path = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if(r < 0 or c < 0 or r >= row or c >= col or board[r][c] != word[i] or (r, c) in path): # 6!
                return False
            path.add((r, c))
            res =(
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            path.remove((r, c)) # 注意这里
            return res
        for r in range(row):
            for c in range(col):
                if dfs(r, c, 0):
                    return True
        return False