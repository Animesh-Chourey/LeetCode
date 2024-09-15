class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        window = 0
        count_zeros = 0
        count_ones = 0
        final = {}

        for index, num in enumerate(nums):
            if num == 0:
                count_zeros += 1
            else:
                count_ones += 1

            # keep track at each index the difference between the countof ones and zeros
            diff = count_ones - count_zeros

            if diff not in final:
                final[diff] = index
            else:
                # get the index at which the same differnce is present from the hash map 
                present_index = final[diff]
                window = max(window, index - present_index) # calculate if at the current index the window is max or not
            
            # for the first instance where the count becomes equal will be from beginning
            if count_ones == count_zeros:
                window = count_ones + count_zeros
        
        return window