class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=0
        profit=0
        while i<len(prices)and j<len(prices):
            if prices[i]<=prices[j]:
                profit = prices[j]-prices[i] if prices[j]-prices[i]>profit else profit
                j+=1
            else:
                i=j
        return profit