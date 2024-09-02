class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        left = 0
        right = len(nums) - 1
        final = []

        while left<=right: #loop will execute until the left and right do not cross each other
            if abs(nums[left]) > abs(nums[right]): # Compare the absolute values of left most and right most element
                final.insert(0, nums[left]**2) # Every element will be added to the 0th index(max element will be added to the end)
                left = left+1
            elif abs(nums[left]) <= abs(nums[right]): # Compare the absolute values of left most and right most element
                final.insert(0, nums[right]**2) # Every element will be added to the 0th index(max element will be added to the end)
                right = right-1
        
        return final