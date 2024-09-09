class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        
        #swap the elements present the start and end index
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            
            # increment start index and decrement end index
            start += 1
            end -= 1