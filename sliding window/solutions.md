# 424. Longest Repeating Character Replacement
**解题思路**  

*滑动窗口*  
- 使用count（hash）来保存每个字母的出现频率，记录最高的次数
- 使用left，right来实现window，用循环更新right，而left的更新条件是：right-left+1-max_frequency的值大于k，意味着需要被替换的字母数已经超过了规定，我们需要移动left来缩小窗口
- res保留最大的长度
<img src = '424.png' width = '500px'>

``` python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0
        max_frequency = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, count[s[right]])
            
            if(right - left + 1 - max_frequency) > k:
                count[s[right]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        return res
```        
# 567. Permutation in String
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.  

### 思路
hash1: 保存s1字母出现次数  
hash2: 保存s2字母出现次数  
hash表都为1-26  
matches: 记录hash1 和 hash2中有多少个字母匹配，注意0 == 0也是匹配的喔  
也就是说, 只要matches == 26, true!  

``` python 
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        hash1, hash2 = [0] * 26, [0] * 26
        
        # initializing hash1 and hash2的前s1长度个元素
        for i in range(len(s1)):
            hash1[ord(s1[i]) - ord('a')] += 1
            hash2[ord(s2[i]) - ord('a')] += 1
        
        # 初始化后当前有多少个字母匹配, 初始化matches
        matches = 0
        for i in range(26):
            matches += (1 if hash1[i] == hash2[i] else 0)
        
        # 滑动窗口策略 
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26: # reach the goal
                return True
            
            # 刚刚加入window的character
            index = ord(s2[right]) - ord('a')
            hash2[index] += 1 # hash2中对应字母数加 1
            if hash1[index] == hash2[index]: 
                matches += 1
            elif hash1[index] + 1 == hash2[index]: #他们之前是相等的，但是加了新的character之后不相等了
                matches -= 1
            
            # 缩小窗口的时候也会影响结果
            index = ord(s2[left]) - ord('a')
            hash2[index] -= 1 #删除hash2中，left pointer指向的值
            if hash1[index] == hash2[index]:
                matches += 1
            elif hash1[index] - 1 == hash2[index]:# 缩小之前他们是相等的，那么缩小之后他们就不相等了，因此总match数减少1
                matches -= 1
            # 移动左窗口
            left += 1
        return matches == 26
```