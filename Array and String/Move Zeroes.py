class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            # Compare the right pointer and if it not equal to 0 replace with left pointer's element
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        