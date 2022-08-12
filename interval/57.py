class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            # not overlapping - new右界小于当前区间的左界, newintervalappend在当前区间前面
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # not overlapping - new左界大于当前区间右界，先append当前区间到res里，剩下的交给循环
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # overlapping
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res