class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right = 0, 1
        maxProfit = 0

        while right<len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        
        return maxProfit


        max_profit = 0
        best_buy = prices[0]                       # lowest price seen so far
        for price in prices[1:]:
            if price > best_buy:
                max_profit = max(max_profit, price - best_buy)
            best_buy = min(best_buy, price)
        return max_profit

        