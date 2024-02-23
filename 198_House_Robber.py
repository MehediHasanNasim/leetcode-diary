class Solution(object):
    def rob(self, nums):
       
        rob1, rob2 = 0, 0 
        for n in nums:
            Temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = Temp
        return rob2
    