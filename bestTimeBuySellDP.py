
# @alexwang4866 - 9 months ago
# Another way to think about it (and why DP is labeled) is ask the question 
# "What is the most money I can make if I sell on each day (where each day is r, or indicated by the right pointer)?" 
# The only thing you would need, is to keep track of the smallest value that came before. 
# This should thoroughly cover each potential case

# Neetcode video - 2 pointer solution - linear scan
# Update L everytime a lower R is seen because that guarantees L is locally minimised? idk


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        localMin = prices[0]
        maxProfit = 0
        
        for day in range(1,len(prices)):
            profit = prices[day] - localMin
            print(f"""Lowest previously seen price: {localMin} \n 
                  Today's price: {prices[day]} \n 
                  Maximally known profit so far: {maxProfit} \n
                  Profit for Day {day}: {profit}
                  """)
            if prices[day] < localMin:
                localMin = prices[day]
            maxProfit = max(maxProfit, profit)
        print(localMin, maxProfit)

        return maxProfit


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))