class Solution(object):
    def singleNumber(self, nums):

        # bit manipulation
        res = 0 
        for n in nums:
            res = n ^ res
        return res

            
            