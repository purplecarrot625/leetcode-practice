class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    # 遍历i前面的所有元素，如果nums[j] < nums[i]，则求一次dp[i] = max(dp[i],dp[j] + 1)
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# 定义dp[i]表示以第i个元素结尾的最长递增子序列长度。那么对于该元素前面的i-1个元素中如果有元素j比nums[i]小，那么dp[i]就等于以元素j结尾的最长递增子序列长度加1，即dp[i] = max(dp[i], dp[j] + 1);遍历i前面的所有元素，只要满足元素j比元素i小，则计算一次dp[i] = max(dp[i], dp[j] + 1)，遍历完成后即可求得dp[i]的最大值，即以第i个元素结尾的最长递增子序列长度。
