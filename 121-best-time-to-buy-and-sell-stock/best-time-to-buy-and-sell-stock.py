class Solution(object):
    def maxProfit(self, prices):
        leastPrice = prices[0]  
        maxProfit = 0            

        for price in prices:     
            if price < leastPrice:
                leastPrice = price   
            profit = price - leastPrice   
            if profit > maxProfit:
                maxProfit = profit   

        return maxProfit
        