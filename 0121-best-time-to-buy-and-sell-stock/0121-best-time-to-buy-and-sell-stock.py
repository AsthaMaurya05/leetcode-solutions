class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        least = prices[0]
        profit = 0
        for i in prices:
            if i < least:
                least = i;
            else:
                profit = max(profit,i-least)
        
        return profit