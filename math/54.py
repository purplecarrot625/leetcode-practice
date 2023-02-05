class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []
        while left < right and top < bottom:
            # row: from left to the right
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            # col: from top to the bottom
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            
            # 这句很关键，如果没有他，会多打出来一个值
            if not (left < right and top < bottom):
                break
            
            # row: from right to the left
            # 注意这里的下标
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1 # 走完了bottom这一行
            
            # col: from bottom to top
            for i in range(bottom - 1, top -1 , -1):
                res.append(matrix[i][left])
            left += 1
        return res
            