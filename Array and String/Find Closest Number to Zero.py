class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        small = nums[0]
        abs_small = abs(nums[0])

        for i in range(1, len(nums)):
            if abs(nums[i]) < abs_small:
                small = nums[i]
                abs_small = abs(small)
            elif abs(nums[i]) == abs_small:
                abs_small = abs(nums[i])
                small = max(small, nums[i])
        
        return small
                
