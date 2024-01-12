class Solution:
    def climbStairs(self, n):
        one, two = 1, 1  # Initialize two variables to store the number of ways for the last two steps
        
        for i in range(n - 1):
            temp = one  # Store the value of 'one' in a temporary variable
            one = one + two  # Update 'one' by adding the number of ways for the last two steps
            two = temp  # Update 'two' with the value previously stored in the temporary variable
        return one  # Return the number of ways to climb 'n' steps

    
    

class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)  # Create a list 'dp' with initial values set to 'amount + 1'.
        dp[0] = 0  # Initialize dp[0] to 0 since zero coins are needed to make up an amount of zero.

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1
