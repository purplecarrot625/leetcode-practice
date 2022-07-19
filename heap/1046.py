import heapq
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
