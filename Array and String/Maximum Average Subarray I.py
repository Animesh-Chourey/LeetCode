class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = left + k -1
        max_avg = - pow(10, 6)

        while right <= len(nums)-1:
            total = 0
            temp = left
            while temp <= right:
                total = total + nums[temp]
                temp = temp + 1
            final = total/k

            if max_avg < final:
                max_avg = final
            
            left = left + 1
            right = right + 1
        
        return max_avg