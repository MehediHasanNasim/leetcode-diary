class Solution(object):
    def buildArray(self, nums):
        res = []

        for i in range(len(nums)):
            val = nums[nums[i]]
            res.append(val)

        return res