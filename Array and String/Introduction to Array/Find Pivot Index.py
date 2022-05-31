class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        flag = 0    # Flag to indicate the equality 
        total_sum = sum(nums) # Total sum of the array
        sum_left=0 #Variable to store the left sum
        for i in range(len(nums)):
            # Right sum equals to the total sum - left sum - the current index value
            sum_right = total_sum - sum_left - nums[i] 
            if sum_left == sum_right:
                flag = 1
                return i
            else:
                sum_left += nums[i]
        
        if flag == 0:
            return -1