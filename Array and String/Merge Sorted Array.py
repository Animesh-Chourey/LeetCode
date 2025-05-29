class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # left pointer at the nums1 array
        left = m - 1  # pointing at the index till numbers to be sorted are present
        # right pointer at the nums2 array 0th index
        right = 0

        # Swap the elements from nums1 and nums2
        # if the elements in nums1 are greater than
        # elements present in nums2 list
        while left > -1 and right < n:
            if nums1[left] > nums2[right]:
                nums1[left], nums2[right] = nums2[right], nums1[left]
                left -= 1
                right += 1
            else:
                break
        
        # nums2.sort()

        # Assign all the values of nums2 to
        # nums1 from the position where only 0 values are present
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i-m]

        nums1.sort()