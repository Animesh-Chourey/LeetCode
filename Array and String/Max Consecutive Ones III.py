class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_count = 0 
        left = 0
        no_flips = 0 # No of zeros encountered and could be flipped

        for right in range(len(nums)):
            if nums[right] == 0: # If the element is 0
                no_flips = no_flips + 1

            while no_flips > k: #if flipping becomes greater than the k amount we need to bring it within limit
                # we will do this by incrementing the left pointer
                if nums[left] == 0:
                    no_flips = no_flips - 1
                
                left = left + 1
            
            count = right - left + 1
            max_count = max(max_count, count)

        return max_count
