class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        final = {}
        count = 0
        
        # create a hash map for all the characters in jewels
        for char_jewels in jewels:
            final[char_jewels] = 0
        
        # eah time the char in stones is present in the hash map
        # increase the count of that char corresponding to the key
        for char_stones in stones:
            if char_stones in final:
                final[char_stones] += 1
        
        # add the values of each key which will represent the number of times each char from jewels appeared in stones
        for key, value in final.items():
            count += value

        return count