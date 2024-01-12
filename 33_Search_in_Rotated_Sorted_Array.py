class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:     # if middle value is the answer
                return mid
            
            # left sorted portion check
            if nums[mid] >= nums[l]:
                # check if target is greater then middle value or less than Left value, =discard the portion
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            # right sorted portion check
            else:
                # check if target is less then middle value or greater than right value, =discard the portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1 
                else:
                    l = mid + 1
                    
        return -1 

