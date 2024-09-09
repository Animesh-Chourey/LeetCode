class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        # check the length of the string after converting it into 'set'
        # and if the length of it = 26 then all the alphabets appeared at least once
        return True if len(set(sentence)) == 26 else False