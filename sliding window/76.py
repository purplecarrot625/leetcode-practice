class Solution:
    def minWindow(self, s: str, t: str) -> str:
        win = defaultdict(int)
        t_dict = defaultdict(int)
        for i in t:
            t_dict[i] += 1
        
        # pointer
        left = 0
        right = 0
        min_len = float('Inf')
        
        # chr_count: 滑动窗口包含的字符数
        chr_count = 0
        
        # min_begain
        begain = 0
        s_len = len(s)
        t_len = len(t)
        
        while right < s_len:
            # 移动窗口
            if t_dict[s[right]] == 0:
                right += 1
                continue
            
            # 滑动窗口包含 t 的字符数，当超过t中字符数，不再增加
            if win[s[right]] < t_dict[s[right]]:
                chr_count += 1
            win[s[right]] += 1
            right += 1
            # 当窗口包含 T 所有的字符时，缩小窗口
            while chr_count == t_len:
                # 这里更新子串的起始位置和长度
                if right-left < min_len:
                    begin = left
                    min_len = right - left
                # 缩小窗口
                if t_dict[s[left]] == 0:
                    left += 1
                    continue
                # 这里表示出窗时，窗口所包含 T 的字符刚好等于 T 中字符的个数
                # 这个时候再移动，窗口就不满足包含 T 所有字符的条件
                # 这里 chr_count - 1 ，循环结束
                if win[s[left]] == t_dict[s[left]]:
                    chr_count -= 1

                win[s[left]]-=1
                left += 1

        return "" if min_len == float('inf') else s[begin:begin+min_len]

# https://juejin.cn/post/6844904166716866568