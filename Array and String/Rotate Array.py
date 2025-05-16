class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''O(n) solution
        
        arr = nums.copy()
        
        for i in range(len(nums)):
            if i+k >=len(nums):
                j = (i+k) % len(nums)
                nums[j] = arr[i]
            else:
                nums[i+k] = arr[i]
        '''
        
        # O(1) Solution
        if k < len(nums):
            k = len(nums) - k
        else:
            k = k % len(nums)
        
        # Reverse the first k elements
        nums[0:k] = nums[0:k][::-1]

        # Reverse the remaining elements
        nums[k:len(nums)] = nums[k:len(nums)][::-1]

        # Now reverse the whole array
        nums[:] = nums[::-1]
        

        return nums

        
        # # Reverse the array
        # start, end = 0, len(nums)-1
        # while start < end:
        #     nums[start], nums[end] = nums[end], nums[start]
        #     start, end = start+1, end-1
        
        # # To make sure k is not out of bounds
        # k = k % len(nums)
        
        # #Reverse the first k elements
        # start, end = 0, k-1
        # while start < end:
        #     nums[start], nums[end] = nums[end], nums[start]
        #     start, end = start+1, end-1
        
        # #Reverse the remaining elements
        # start, end = k, len(nums) - 1
        # while start < end:
        #     nums[start], nums[end] = nums[end], nums[start]
        #     start, end = start+1, end-1
            
    