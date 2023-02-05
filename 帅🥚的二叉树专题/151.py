class Solution:
    def reverseWords(self, s: str) -> str:
        # 整体反转 then 逐步反转
        
        # 1. 去除多余空格
        # 2. 反转整个字符串
        # 3. 反转每个单词
        s = self.removeSpace(s)
        s = self.reverseString(s)
        s = self.reverseWord(s)
        
        return ''.join(s)
    def removeSpace(self, s):
        l, r = 0, len(s) - 1
        
        # remove the front spaces
        while l < r and s[l] == ' ':
            l += 1
        while l < r and s[r] == ' ':
            r -= 1
        new_s = []
        
        # remove extra space between each words
        while l <= r:
            if s[l] != ' ':
                new_s.append(s[l])
            elif s[l] == ' ' and new_s[-1] != ' ':
                new_s.append(s[l])
            l += 1
        return new_s
        
    def reverseString(self, s):
        # l, r pointer
        l, r = 0, len(s) - 1
        while l < r: # <
            s[l], s[r] = s[r], s[l]
            
            # move the pointer
            l += 1
            r -= 1
        return s
    def reverseWord(self, w):
        l, r = 0, 0
        n = len(w)
        
        while l < n:
            while r < n and w[r] != ' ':
                r += 1
            w[l:r] = self.reverseString(w[l:r])
            
            # reverse the next word
            l = r + 1
            r += 1
        return w