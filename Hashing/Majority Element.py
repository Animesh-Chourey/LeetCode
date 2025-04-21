class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements_count = {}

        for num in nums:
            if num in elements_count:
                elements_count[num] += 1
            else:
                elements_count[num] = 1
        
        for key, val in elements_count.items():
            if val > len(nums)//2:
                return key