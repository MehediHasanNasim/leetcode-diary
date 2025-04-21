class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        min_val = 0
        max_val = 0
        curr_val = 0

        for n in differences:
            curr_val += n
            min_val = min(min_val, curr_val)
            max_val = max(max_val, curr_val)
        
        count = (upper - lower) - (max_val - min_val) + 1

        return count if count > 0 else 0