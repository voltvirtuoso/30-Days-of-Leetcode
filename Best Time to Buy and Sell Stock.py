class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_p, min_p = 0, prices[0]
        for price in prices[1:]:
            max_p = max(max_p, price - min_p)
            min_p = min(min_p, price)
        
        return max_p
