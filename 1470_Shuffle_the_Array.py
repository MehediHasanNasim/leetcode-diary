class Solution(object):
    def shuffle(self, nums, n):
        # using loop
        res = []

        for i in range(n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res


        # Bit manipulation
        for i in range(n):
            nums[i] = nums[i] << 10
            nums[i] = nums[i] | nums[i + n]
        
        j = 2 * n - 1
        for i in range(n - 1, -1, -1):
            y = nums[i] & (2**10 - 1)
            x = nums[i] >> 10
            nums[j] = y
            nums[j - 1] = x
            j -= 2
        return nums
