class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        final = [-1] * len(nums) # initialise all elements of final with -1 
        window = (2*k) + 1 
        left = 0
        right = 0
        total = 0

        # if the window is bigger than the length or k elements needed are greater than the length
        # the final should be returned as -1
        if k >= len(nums) or window>len(nums):
            return final
        else:
            # get the sum of the elements present in the window
            for right in range(window):
                total += nums[right]
            

            while right < len(nums):
                final[right-k] = total//window # this will give the weighted average of the range of k elements

                right += 1
                if right < len(nums) and left < len(nums):
                    total += nums[right] # shift the right index by 1 and add the index's value
                    total -= nums[left] # shift the left index by 1 and subtract the index's value
                left += 1
            
            return final

        # This code is giving time exceeding error


        # small = k
        # large = len(nums) - k
        # left = 0
        # sums = 0

        # final = []

        # for i in range(len(nums)):
        #     right = i

        #     if right >= large or right < small:
        #         final.append(-1)
        #         sums += nums[right]
        #     else:
        #         total = sums
        #         sums += nums[right]
        #         temp = k + right

        #         while right <= temp:
        #             total += nums[right]
        #             right += 1
                
        #         weightedAvg = total//((2*k)+1)
        #         final.append(weightedAvg)
            
        #         sums -= nums[left]
        #         left += 1
        
        # return final