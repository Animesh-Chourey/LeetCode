class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        largestSum = float(-inf)
        
        for i in range(len(nums)):
            total += nums[i]
            
            # Compare the total with maximum sum
            largestSum = max(largestSum, total)

            # if the total gets smaller than 0, restart from the next element again
            if total < 0:
                total = 0
                continue
            
        
        return largestSum