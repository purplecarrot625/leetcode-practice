class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # 两个字符长度相等 and 当前串等于字典里的w串 啊想吃烤串
                if(i + len(w) <= len(s) and s[i: i + len(w)]) == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]