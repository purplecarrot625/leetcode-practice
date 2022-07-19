import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        pts = []
        
        for x, y in points:
            distance = (abs(x - 0) ** 2) + (abs(y - 0) ** 2)
            pts.append([distance, x, y])
        
        result = []
        heapq.heapify(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            result.append([x, y])
        return result