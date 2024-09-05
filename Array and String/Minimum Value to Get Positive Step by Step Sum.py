class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 0
        total = 0
        flag = 0 # to indicate the total never went negative

        if nums[0] < 1: #if the first number is negative 
            startValue = abs(nums[0]) + 1 #take absolute and add it with 1 odicating total will be minimum of 1 when addition starts
            total = startValue
            flag = 1 # if the total is changed even once the flag is changed
        
        for i in range(len(nums)):
            total += nums[i]

            if total < 1:
                startValue += abs(total) + 1 # the absolute number will give the range with which startValue needs to be incremented
                total = 1 # this is set to 1 indicating the once startValue is changed the minimum it will bring total to is 1
                flag = 1
        
        # if the flag remains 0 then all the elements in the array were positive
        if flag == 0:
            startValue = 1
 
        return startValue