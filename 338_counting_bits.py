class Solution(object):
    def countBits(self, n):
        dp = [0] * (n + 1)  # initialise value with 0 & (n+1) (length of list) means how many time we gonna compute
        offset = 1    # for highest power of two
        
        for i in range(1, n + 1):
            if offset * 2 == i:   # 1*2=2, so its update offset = 2, after that 2*2=4, then its update offset to 4.
               offset = i
            dp[i] = 0 + dp[i - offset]  # for every value of n, its count the number of 1 in binary's. 
            
        return dp


    
    
    
    
    
    
    
    
    
    
    