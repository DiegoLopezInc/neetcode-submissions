class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        b, s = 0,1
        maxP = 0
        while s < len(prices):
            p = (prices[s] - prices[b])
            
            maxP = max(p, maxP)
            
            if p < 0 and s != len(prices)-1:
                b = s
            else:
                s+=1
        return maxP

            
        
