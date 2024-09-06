class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        small = k
        large = len(nums) - k
        left = 0
        sums = 0

        final = []

        for i in range(len(nums)):
            right = i

            if right >= large or right < small:
                final.append(-1)
                sums += nums[right]
            else:
                total = sums
                sums += nums[right]
                temp = k + right

                while right <= temp:
                    total += nums[right]
                    right += 1
                
                weightedAvg = total//((2*k)+1)
                final.append(weightedAvg)
            
                sums -= nums[left]
                left += 1
        
        return final