class Solution(object):
    def findMin(self, nums):
        res = nums[0] # assume the minimum is left most value
        left, right = 0, len(nums) - 1 # left most and right most value
        
        while left <= right:
            if nums[left] < nums[right]:  #if that array is already sorted as subarray
                res = min(res, nums[left])
                break 
            mid = (left + right) // 2  # mid value find out
            res = min(res, nums[mid])  # checking mid value, if it is the minimum or not
            
            if nums[mid] >= nums[left]:   # if the mid is part of left sorted nums then go for to look right sorted nums
                left = mid + 1
            else:
                right = mid - 1     
        return res
            





















            
            