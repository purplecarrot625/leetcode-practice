# 746. Min Cost Climbing Stairs
最精彩的一步是在cost后面加了个0，方便计算
[20, 1, 3] 0
``` python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])
        

```