class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Solution 1

	visited = {}

        for i, val in enumerate(nums):
            diff = target - val # Take the difference

            # If the difference is not present
            # Update the value and index as key value pair respectively
            if diff not in visited:
                visited.update({val: i})
            else:
                return [i, visited[diff]]
        
	# Solution 2

        # final = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] + nums[j] == target:
        #             final.append(i)
        #             final.append(j)
        #             return final