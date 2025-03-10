class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        left = 0
        right = 1
        final = []

        # Sorting the list based on the first element
        intervals.sort(key=lambda x: x[0])

        # if the intervals list is empty or contains only one element
        if len(intervals) == 1 or len(intervals) == 0:
            final = intervals
        else:
            while right < len(intervals):

                if not final:
                    final.append(intervals[left])
                    # left += 1
                    continue
                # if the next index first element becomes greater than
                # current index second element of final list
                # append the elements at next index to the final list
                elif final[left][1] < intervals[right][0]:
                    final.append(intervals[right])
                    left+=1
                # compare the min and max to update the elemets that are overlapping
                elif final[left][1] >= intervals[right][0]:
                    final[left][1] = max(final[left][1], intervals[right][1])
                    final[left][0] = min(final[left][0], intervals[right][0])

                right += 1
        
        return final