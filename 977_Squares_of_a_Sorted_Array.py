class Solution(object):
    def sortedSquares(self, nums):
    
        #using loop
        res = []
        for i in nums:
            res.append(i*i)
        return sorted(res)
            
        # short way of looping
        squares = [i*i for i in nums] 
        return sorted(squares)

        # two pointer solution
        res = []
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r -= 1
        return res[::-1]