class Solution(object):
    def maxProduct(self, nums):
        result = max(nums) # zero is not the exact value for default value
        curMin, curMax = 1, 1  # its not effect the multiplying
        
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1 # set the value if n = 0
                continue
            
            temp = n * curMax
            curMax = max(n * curMax, n * curMin, n) # only store max value
            curMin = min(temp, n * curMin, n) # only store min value
            
            result = max(result, curMax)
        return result
    
# class Solution(object):
#     def maxProduct(self, nums):
#         result = max(nums)
#         curMin, curMax = 1, 1
#         for n in nums:
#             if n == 0:
#                 curMin, curMax = 1, 1
#                 continue
#             temp = n * curMax
#             curMax = max(n * curMax, n * curMin, n)
#             curMin = min(temp, n * curMin, n)
#             result = max(result, curMax)
#         return result
            
    
    
    
    
    
    
    
    
    