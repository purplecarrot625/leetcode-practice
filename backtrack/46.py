class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # base case
        if (len(nums) == 1):
            return [nums[:]] # copy of the nums
        
        for i in range(len(nums)):
            n = nums.pop(0) # pop the first element
            perms = self.permute(nums) # 是一个二维数组，be like: [[2,3],[3,2]]
            
            for perm in perms:
                perm.append(n) # be like:[2,3,1] [3,2,1]
                res.append(perm)
            nums.append(n) # 接下来还要用 1, and nums[1,2,3] 变成了 [2,3,1], pop(0)就该pop出2了
        return res