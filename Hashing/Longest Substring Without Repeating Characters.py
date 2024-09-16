class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        final = {}
        max_window = 0
        left = 0
        right = 0

        # loop through until right pointer becomes equal to the length of the length
        # and until left pointer is smaller than right 
        while right < len(s) and left <= right:
            if s[right] not in final: # add the char if it not present in the hash map
                final[s[right]] = 1
                right += 1
            else:
                # delete the char present at the left pointer
                del final[s[left]]
                left += 1
            
            window = right - left
            max_window = max(max_window, window)
        
        return max_window
        # for right in range(len(s)):
            

        # for char in s:
        #     if char not in final:
        #         final[char] = final.get(char, 0) + 1
        #         count += 1
        #         max_count = max(count, max_count)
        #     else:
        #         final.clear()
        #         final[char] = final.get(char, 0) + 1
        #         count = 1
            
        # return max_count