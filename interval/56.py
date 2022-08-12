class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn)
        intervals.sort(key = lambda i: i[0]) # sort by the 左区间
        output = [intervals[0]]
        
        # iterate every element in intervals in sorted order
        for start, end in intervals[1:]:
             # most recent interval, and get the end of it
                lastEnd = output[-1][1]
                if start <= lastEnd: # Merge them!
                    output[-1][1] = max(lastEnd, end) # be like: [1,5], [2,4] => [1,2,4,5], we wanna keep 5
                else: # non-overlapping
                    output.append([start, end]) # be like: [1,5],[7,8] => [1,5],[7,8]
        return output