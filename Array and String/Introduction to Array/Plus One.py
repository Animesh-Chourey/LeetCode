class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum = 0
        for i in digits: # sum of all the elements 
            sum = (sum*10) + i
            
        sum += 1
        new_digits = []
        while sum > 0:
            r = sum % 10 #Get the last digit
            new_digits.insert(0,r) #insert it into the 0th index
            sum = sum // 10 #Get all the digits except the last one 
        
        return new_digits