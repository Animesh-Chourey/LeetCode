class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0

        # Sum of the first k elements
        for i in range(k):  
            total = total + nums[i]
        
        max_avg = total / k #taking the avg of first k elements

        for i in range(k, len(nums)):
            total = total - nums[i-k] # Subtracting the last skipped element after incrementing by 1
            total = total + nums[i] # Adding the new added element after incrementing 

            new_avg = total / k # Calculating the new avg

            max_avg = max(max_avg, new_avg) # Comparing the previous maximum avg and new avg after incrementing
        
        return max_avg