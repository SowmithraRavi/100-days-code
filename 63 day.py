class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini= prices[0]
        m = 0
        
        for price in prices[1:]:
            m = max(m, price - mini)
            mini = min(mini, price)
            
        return m
        
