class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rightmax = [0] * len(prices)
        rightmax[-1] = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            rightmax[i] = max(rightmax[i+1], prices[i])

        maxprofit = 0
        for i in range(len(prices)-1):
            profit = rightmax[i+1] - prices[i]
            if profit > maxprofit:
                maxprofit = profit
        
        return maxprofit