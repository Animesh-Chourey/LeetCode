class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        num = x

        # if a number is negative it wont be palindrome
        if x < 0:
            return False

        # loop until number is greater than zero
        while x > 0:
            s = x % 10 # Get the number present at the ones position
            reverse = (reverse * 10) + s 
            x = x // 10 # remove the number present at the ones position

        if num == reverse :
            return True