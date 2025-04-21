class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
            elif num > target:
                return i
            elif len(nums)-1 == i:
                return len(nums)