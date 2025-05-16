class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_count = {} # keep track of the count of each number in the list

        for n in nums:
            if n not in num_count: # if the num is not present increment its value
                num_count[n] = num_count.get(n, 0) + 1
            else:
                num_count[n] += 1
        
        for key, value in num_count.items():
            if value != 2:
                return key