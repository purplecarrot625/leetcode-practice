# 77. Combinations
典型的backtrack题
``` python
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        resList = []
        if k == 0:
            return [[]]
        
        # backtrack是一个递归调用的过程
        def backtracking(start):
            if len(resList) == k: # 只剩k个元素
                temp = resList[:]
                res.append(temp)
            for i in range(start, n + 1):
                resList.append(i)
                backtracking(i + 1)
                resList.pop()
        backtracking(1)
        return res

```