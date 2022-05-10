class Solution:
    
    """
    Solution via DP/memoization.
    
    This can be solved in one pass via the "best run" technique. The initial "best profit" 
    is basically non-existent, since you are at a financial deficit after buying the first stock.
    We then loop through all the possible buy/sell dates, keeping track of the profits that could 
    be made at each sell date given the current buy date. Any time we encounter a cheaper buy
    date, that becomes the new buy date. This is OK because any profit that can be made beyond
    that point will be optimized by choosing the cheapest buy date up to that point. This will
    guarantee that we eventually come across the "best profit", which we then return.
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    
    def maxProfit(self, prices: List[int]) -> int:
        buy_date = 0
        best_profit = -prices[buy_date]
        
        for sell_date in range(1, len(prices)):
            profit = prices[sell_date] - prices[buy_date]
            if profit > best_profit:
                best_profit = profit
            if prices[sell_date] < prices[buy_date]:
                buy_date = sell_date
                
        if best_profit < 0:
            return 0
        else:
            return best_profit
        