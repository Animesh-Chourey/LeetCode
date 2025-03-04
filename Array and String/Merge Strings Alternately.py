class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ""
        # Get the length of the smaller word
        len_small_word = len(word1) if len(word1) < len(word2) else len(word2)
        # Get the word with larger length
        large_word = word2 if len(word1) < len(word2) else word1

        # iterate with length of smaller word
        for i in range(len_small_word):
            final += word1[i]
            final += word2[i]
        
        # if the length is not equal of both words
        # append the remaining letters of the larger word into final
        if len(word1) != len(word2):
            final += large_word[len_small_word:]

        return final