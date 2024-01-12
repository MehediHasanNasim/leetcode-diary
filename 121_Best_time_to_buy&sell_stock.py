class Solution(object):
    def maxProfit(self, prices):
        buy, sell = 0, 1  # we can sell before we buy. So, its 0 after 1
        maxP = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:          # checking profitable?
                profit = prices[sell] - prices[buy]
                maxP = max(maxP, profit)            # updating the max value
            else:
                # if the amount is lower then that should be buying price
                buy = sell
            sell += 1                               # checking next value
        return maxP
