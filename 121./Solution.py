class Solution(object):
           
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        


        mn = min(prices)


        if min(prices) == prices[len(prices)-1] and prices == sorted(prices, reverse=True):
  
            return 0

        elif min(prices) == prices[len(prices)-1] and prices[:-1] == sorted(prices[:-1]):
              mn = min(prices[:-1])
              mx = max(prices)
              return mx-mn

        else:
        
            #print("else")
            #return 1
          
            mx = max(prices[prices.index(mn)+1:])
            return mx-mn
                

           
            


        
