# 1046. Last Stone Weight

 python中没有最大堆, 只有最小堆, 所以我们可以变成负数推进去

 ``` python
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            
            if first < second:
                mashed = first-second  
                heapq.heappush(stones, mashed)
        stones.append(0) # if the stones is empty,return 0, else return the value of stones[0]
        return abs(stones[0])

 ```