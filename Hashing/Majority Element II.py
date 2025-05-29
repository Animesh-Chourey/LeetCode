class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter1, counter2 = 0, 0
        num1, num2 = float('-inf'), float('-inf')
        final = []

        # Given the limit there can be atmost 2 elements with more than n/3 appearences
        for num in nums:
            if counter1 == 0 and num2 != num:
                counter1 = 1
                num1 = num
            elif counter2 == 0 and num1 != num:
                counter2 = 1
                num2 = num
            elif num1 == num:
                counter1 += 1
            elif num2 == num:
                counter2 += 1
            else:
                counter1 -= 1
                counter2 -= 1
        
        # After the iteration, check if occurence of num1 and num2 elements
        # Is actually greater than n/3 times
        limit = int(len(nums)/3) + 1
        counter1, counter2 = 0, 0
        for num in nums:
            if num == num1:
                counter1 += 1
            if num == num2:
                counter2 += 1

        if counter1 >= limit:
            final.append(num1)
        if counter2 >= limit:
            final.append(num2)
        
        return final