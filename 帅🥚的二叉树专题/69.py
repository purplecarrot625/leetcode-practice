class Solution:
    def mySqrt(self, x: int) -> int:
        # 返回 res*res <=x 的最大值
        if x == 0 or x == 1:
            return x
        l,r ,res = 1, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res