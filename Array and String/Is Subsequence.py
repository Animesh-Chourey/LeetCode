class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        for i in s:
            for j in range(len(t)):
                # if the letter i is in t
                # increment the k
                # take the subset of t after the j index where i was found 
                if i == t[j]:
                    k += 1
                    t = t[j+1:]
                    break
        
        # return true if k == len(s) else return false
        if k == len(s):
            return True
        else:
            return False