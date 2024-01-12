class Solution(object):
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)      # (amount + 1)= length of amount(0...amount),[amount + 1] = maximum value default set. or Create a list to store minimum coin counts, initialized to a value greater than the maximum amount.
        dp[0] = 0       # Setting the minimum number of coins needed to make an amount of 0 as 0.
        
        for a in range(1, amount + 1):    # Iterate through all amounts from 1 to the target amount.
            for c in coins:               # brute force & Check if the current coin denomination can be used to make up the current amount a.
                if a - c >= 0:            # checking negative & if the current coin denomination can be used to make up the current amount a.
                    dp[a] = min(dp[a], 1 + dp[a - c])  # possibly found the solution, Update the minimum coin count for the current amount a by choosing the minimum between its current value and 1 + the minimum coin count for amount (a - c).
         
        return dp[amount] if dp[amount] != amount + 1 else -1 # If the minimum coin count for the target amount is still initialized to a value greater than the maximum amount, return -1. Otherwise, return the minimum coin count.




























