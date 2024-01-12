class Solution(object):
    def maxSubArray(self, nums):
        maxSub = nums[0] # initial the first value
        currentSum = 0
        
        for n in nums:      # checking the all vaiues
            if currentSum < 0:
                currentSum = 0  # if value is negative then Currentsum will return to Zero
            
            currentSum += n      # addition 
            
            maxSub = max(maxSub, currentSum) # updating the maxnumber
            
        return maxSub
            