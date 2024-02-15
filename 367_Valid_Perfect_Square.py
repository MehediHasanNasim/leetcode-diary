class Solution(object):
    def isPerfectSquare(self, num):
    
        # binary search
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                l = mid + 1
            else:
                r = mid - 1
        return False


        # brute force >> though- here memory extend crossing
        for i in range(1, num + 1):
            if i*i == num:
                return True
            elif i*i > num:
                return False