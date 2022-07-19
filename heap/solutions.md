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

 # 973. K Closest Points to Origin
 Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

### 思路
用loop计算出所有的距离，压到list里面，然后用heapify排序，对k个元素，pop出result  

``` python
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        pts = []
        
        for x, y in points: # for x,y
            distance = (abs(x - 0) ** 2) + (abs(y - 0) ** 2) # 不用算开平方就可以比较啦
            pts.append([distance, x, y]) # 注意这里list append是一个[]
        
        result = []
        heapq.heapify(pts) # 堆排序
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            result.append([x, y])# list append是[]
        return result
```

# 215. Kth Largest Element in an Array
上一题是写closet元素，也就是从小弹出，但是这一题要从最大元素开始弹出，那么用heapify怎么实现呢？应该是不可以了
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.  
采用快速排序的思路，每次遍历后返回pivot（快速排序中的专有名词）的位置，如果该位置不是k，则对新的更小的数组执行快速排序操作，依次类推，直到pivot的位置是k为止。
#### quick select algorithm
``` python
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # nums.sort()
        # return nums[len(nums) - k]
        
        k = len(nums) - k # index
        def quickSelect(l, r):
            # pivot->right most position value
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p] # swap the value
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k:
                return quickSelect(l, p - 1)
            elif p < k:
                return quickSelect(p+1, r)
            else:
                return nums[p]
        return quickSelect(0, len(nums) - 1)
```