class Solution(object):
    def countSubarrays(self, nums):
        res = 0
        for n in range(len(nums) - 2):
            if (nums[n] + nums [n + 2]) * 2 == nums[n + 1]:
                res += 1
        return res