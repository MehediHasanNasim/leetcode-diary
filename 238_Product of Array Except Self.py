class Solution(object):
    def productExceptSelf(self, nums):
        result = [1] * (len(nums))  #values in nums storing in res as initail value 1
        
        prefix = 1 #assume the value
        for i in range(len(nums)):   # looping to all value
            result[i] = prefix  # update the latest prefix value. 
            prefix *= nums[i] # multiplying those prefix values & storing value to result
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1): # reversing the index value
            result[i] *= postfix 
            postfix *= nums[i]
            
        return result
    
 
# class Solution(object):
#     def productExceptSelf(self, nums):
#         result = [1]* len(nums)
        
#         prefix = 1
#         for i in range(len(nums)):
#             result[i] = prefix
#             prefix *= nums[i]
            
#         postfix = 1 
#         for i in range(len(nums)-1,-1,-1):
#             result[i] *= postfix
#             postfix *= nums[i]
            
#         return result
    
    
    
    
    
    
    
    
            
            