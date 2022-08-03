class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        
        def backtrack(i, subset):
            if i == len(nums): # means that we have gone through the entire array
                res.append(subset[:]) # avoid overwriting
                return

            # all subsets that includes nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
        
            # duplicate! All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, []) #一开始的subset是[]，一点点构建
        return res