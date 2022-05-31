class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        index_maxNum = nums.index(max_num)
        
        # Method 1
        #Sort the array in desceding order
        nums.sort(reverse=True)
        if len(nums)==1:
            return 0
        if  nums[0] < (2*nums[1]): # We only need to check the first two elements
            return -1
        else:
            return index_maxNum
        
        
        # Method 2
        # flag = 1        
#         for i in nums:
#             if i == max_num:
#                 continue
#             else:
#                 if max_num < (2*i):
#                     flag = 0
#                     return -1
        
#         if flag == 1:
#             return index_maxNum
