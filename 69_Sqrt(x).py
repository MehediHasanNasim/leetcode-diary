class Solution(object):
    def mySqrt(self, x):
        
        # Binary search
        l, r = 0, x
        res = 0
        while l <= r:
            m = (l + r)// 2
            if m*m == x:
                return m
            elif m*m > x:
                r = m - 1
            else:
                l = m + 1
                res = m
        return res


             