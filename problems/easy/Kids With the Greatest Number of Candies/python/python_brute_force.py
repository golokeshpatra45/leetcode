class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candies = max(candies)        
        final = [True if candies[i]+extraCandies >= max_candies else False for i in range(len(candies)) ]

        return final
        
