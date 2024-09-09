class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        final = [-1] * (len(nums)+1) # adding one new element because there is 1 number missing
        left = 0
        right = len(final) - 1

        # update the number in final
        # by iterating through the nums and updating the index of final for the number that we got from nums while iterating
        for i in range(len(nums)):
            final[nums[i]] = nums[i]
        
        # loop through final and check the element which is still -1
        # that element is the number missing from nums
        while left <= right:
            if final[left] == -1:
                return left
            elif final[right] == -1:
                return right
            
            left += 1
            right -= 1