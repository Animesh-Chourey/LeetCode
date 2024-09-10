class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        final = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0} # keys as all the unique chars needed in 'balloon'
        min_val = float('inf')

        for ch in text:
            if ch in final: # for each key,if the character present in the text is same increment the number of times it appears
                final[ch] += 1
        
        for val in final.values():
            if val == 0: # if any of the key's counter check is 0, that means there won't be balloon present in the text even once 
                return 0
        
        for index, val in final.items():
            if index == 'b' or index =='a' or index =='n':
                min_val = min(min_val, val) #take the minimum value of counter, which represents the maximum number of time "balloon can be made"
            else:
                min_val = min(min_val, val//2)

        return min_val