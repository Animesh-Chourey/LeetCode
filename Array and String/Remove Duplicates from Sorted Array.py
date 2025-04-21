class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
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