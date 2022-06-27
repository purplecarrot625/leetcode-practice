class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        res = 0
        
        while right < len(nums) - 1:
            farthest_distance = 0
            for i in range(left, right + 1): # make the right inclusive
                farthest_distance = max(farthest_distance, i + nums[i])
            left = right + 1
            right = farthest_distance
            res += 1
        return res