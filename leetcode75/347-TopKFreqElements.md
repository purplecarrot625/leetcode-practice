# Top K frequent elements

### freq 的index表示频率
[ [ ], [ ], [ ], [ ] ]

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n,0) + 1
        for n,c in count.items():
            freq[c].append(n) # n occurs c times
        res = []

        # descending order
        for i in range(len(freq) - 1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
```