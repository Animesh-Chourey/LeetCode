class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        final = [1] * len(nums)
        postf = 1
        pref = 1
        # Iterate over the nums list two times

        # While iterating first time take the prefix multiplication of the list
        for i in range(len(nums)):
            final[i] = pref
            pref *= nums[i]

        # During second iteration perform the postfix multiplication
        # in reverse order
        # and update the results with final list
        for i in range(len(nums)-1, -1, -1):
            final[i] *= postf
            postf *= nums[i]
        
        return final
