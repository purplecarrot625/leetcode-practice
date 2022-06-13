# 解题思路和笔记

## 242. Valid Anagram
### 注意：
* 这个不是反转列表！这个问题是rearrange

### 😍 Solution 1: Sort the two Strings.

``` Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
```

### 😍 Solution 2: Count the occurrence of characters (HashMap)

Time complexity O(s+t)

``` python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            # avoid the keyvalue error
            countS[s[i]] = countS.get(s[i],0) + 1
            countT[t[i]] = countT.get(t[i],0) + 1
       
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
            
        return True
```

## Two sum
O(n) with HashMap
``` python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val -> index
        
        for i, n in enumerate(nums):
            diff = target - n # check difference
            if diff in prevMap:
                return [prevMap[diff], i] #solution
            prevMap[n] = i
```
### HashTable in Python


## Group Anagrams
O(mn) m is the number of input strings, n is the average length of each string

* 如何判断是一组的？
  - 统计每个string中字母的出现频次 （count=[0]*26）
* 怎么存？
  - hashmap->res = defaultdict[list]

💡*defaultdict接受一个工厂函数作为参数
这个factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值*

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = collections.defaultdict(list) # 当key不存在时生成默认的，防止出错
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1 #把'a' map到index 0
            result[tuple(count)].append(s) # python中list不能当作key，所以把list转成tuple
        
        return result.values() # 注意这是values
```