class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = float('inf')
        maximum = 0

        for price in prices:
            #check each price and if it is min than before assign it to min_value
            if min_value > price:
                min_value = price
            
            diff = price - min_value

            #if the difference is greater, assign that value to max
            if diff > maximum:
                maximum = diff
            
        return maximum