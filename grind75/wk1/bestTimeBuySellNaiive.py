class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = []
        
        for i,dayBuy in enumerate(prices):
            for j, daySell in enumerate(prices):
                if j > i:
                    profits.append(daySell - dayBuy)
        
        return max(max(profits),0)  

sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))