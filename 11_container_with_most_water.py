class Solution(object):
    def maxArea(self, height):
        # BRUTE Force algorithm that will give run time error.
        # res = 0
        # for l in range(len(height)):
        #     for r in range(l + 1, len(height)):
        #         area = (r - l) * min(height[l], height[r])
        #         res = max(res, area)
        # return res
        
        # two pointer solution?
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)         # rectangular area formula
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res