class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)

        return True if len(nums) != len(nums_set) else False