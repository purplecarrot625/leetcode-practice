class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n #创建最下层, and因为都是1条路径, 所以值为1
        
        for i in range(m-1): # 一层一层循环, 从bottom to top
            newRow = [1] * n # 当前层
            for j in range(n - 2, -1, -1): # 循环列, 从右到左
                newRow[j] = newRow[j + 1] + row[j] # row保存的是down值, newrow[j+1]保存的是rigtht值
            row = newRow # 将当前层保存
        return row[0]