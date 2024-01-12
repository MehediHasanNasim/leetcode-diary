class Solution(object):
    def threeSum(self, nums):
        res = []  # have to return result as a list of lists
        nums.sort() # sort the input array 
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # dont wanna use same value of a in same position. if it fill those conditions thats means the same value come twice.
                 
                continue # to next iteration
            # apply two sum conditions
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # update the next value of a, so we can recheck more probability of conditions
                    l += 1
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1 
        return res


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    