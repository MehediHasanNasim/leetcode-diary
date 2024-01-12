class Solution(object):
    def missingNumber(self, nums):
        res = len(nums)
        for i in range(len(nums)):      # checking index 
            res += (i - nums[i])   # adding index as i and minus it by the value of index. & update it in res
        return res
    