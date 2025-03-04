class Solution:
    def romanToInt(self, s: str) -> int:
        dict_letters = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        i = 0
        total = 0
        num_letters = len(s)

        while i < num_letters:
            # if the value at i index is less than i+1 index
            # substract the i index hash value and add the i+1 hash value
            if i < num_letters-1 and dict_letters[s[i]] < dict_letters[s[i+1]]:
                total += dict_letters[s[i+1]] - dict_letters[s[i]]
                i += 2
            else:
                total += dict_letters[s[i]]
                i += 1
        
        return total