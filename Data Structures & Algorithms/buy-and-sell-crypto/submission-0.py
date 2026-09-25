class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(0, len(prices)-1):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                profit = sell - buy 
                max_profit = max(max_profit, profit)

        return max_profit
