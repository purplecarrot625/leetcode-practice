# 74. Search a 2D Matrix
非常值得收藏的二分查找 and 记模板啊!  
double binary search
O(logm)+O(logn) 
up-bottom binary seach
left-right binary search

``` python
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        
        #注意这里row-1
        top, bot = 0, row - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        
        row = (top + bot) // 2
        # 记忆方法: 大于左指针+，小于右指针减
        l,r = 0, col - 1
        while l <= r:
            m = (l + r) //2 #middle
            if target > matrix[row][m]:
                l = m + 1 
            elif target < matrix[row][m]:
                r = m - 1
            else:# target等于middle表示找到了
                return True
        return False
            
```

# 875. Koko Eating Bananas
碎碎念:  
吃香蕉，话说为什么不是每次能吃很多是最少呢？  
看题！ Return the minimum integer k such that she can eat all the bananas within h hours.  
我们要找出，在规定时间内能吃完的最小速度  
