class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
	# Solution 1

	left = 0
        # if the element at right position is greater than element at left position
        # swap that greater element with the element after the left index position
        for right in range(1, len(nums)):
            if nums[left] < nums[right]:
                nums[left+1], nums[right] = nums[right], nums[left+1]
                left += 1
        
        return left+1


	# Solution 2	

	left = 0
        right = 1

        # iterate until left index encounters 'A'
        # and until right inde does not exceed the range of nums
        while nums[left] != 'A' and right <= len(nums) -1:
            if nums[left] == nums[right]:
                # if the same element occurs pop the element at right index and in exchange append 'A'
                nums.pop(right)
                nums.append('A')
                continue
            else:
                left += 1
                right += 1
        
        # calculate the total numbers present
        counter = 0
        for num in nums:
            if num == 'A':
                break
            else:
                counter += 1

        return counter