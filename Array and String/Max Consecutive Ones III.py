class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count = 0
        
        for i in range(len(nums)):
            no_flips = 0
            temp = 0
            count = 0

            while no_flips<=k and temp<=len(nums):
                if nums[i] == 1:
                    count += 1
                    temp += 1
                else:
                    no_flips += 1
                    count += 1
                    temp += 1
            
            max_count = max(max_count, count)
        
        return max_count