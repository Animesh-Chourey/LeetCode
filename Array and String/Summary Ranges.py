class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        i = 0
        final = [] 
        
        while i < len(nums): 
            left = nums[i]

            # the list will iterate as long as as
            # the i does not go out of bounds
            # and element at i+1 index is 1 greater than the element at i index
            while i < len(nums)-1 and nums[i] + 1 == nums[i + 1]: 
                i += 1 
            
            # the inconsistency to append to final list
            
            # if there is interval between the left value and value at i position
            if left != nums[i]: 
                final.append(str(left) + "->" + str(nums[i]))
            else: 
                final.append(str(nums[i]))
            
            i += 1

        return final