class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_index, neg_index = 0, 1
        final = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0: # positive elements will go to even indices
                final[pos_index] = nums[i]
                pos_index += 2
            else: # n3gative elements will go to odd indices
                final[neg_index] = nums[i]
                neg_index +=  2
        
        return final