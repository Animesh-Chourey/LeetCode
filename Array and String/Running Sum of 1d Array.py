class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        final = []
        total = 0

        for i in range(len(nums)):
            total += nums[i] #add each new element to the total
            final.append(total) # append it to the final list
        
        return final
