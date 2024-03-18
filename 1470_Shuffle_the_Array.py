class Solution(object):
    def shuffle(self, nums, n):
        # using loop
        res = []

        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
