class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        ans = numBottles

        while(numBottles>=numExchange):
            newb = numBottles//numExchange

            rem = numBottles%numExchange
            ans += newb
            numBottles = newb + rem
        return ans    
        