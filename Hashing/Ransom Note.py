class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_track = {}

        # for every character in magazine
        # create a hashmap/dict for the number of times each character is present in magazine
        for char in magazine:
            if char not in char_track:
                char_track[char] = char_track.get(char, 0) + 1
            else:
                char_track[char] += 1
        
        flag = 0
        for char in ransomNote:
            if char not in char_track:
                return False
            else:
                # if the char is present decrement the count and increment the flag to keep track of number of characters
                char_track[char] -= 1
                flag += 1

                if char_track[char] == 0: # if any character count becomes 0, remove that character from char_track
                    del char_track[char]
        
        # if the flag is equal to length of ransomNote then all the elements are present 
        if flag == len(ransomNote):
            return True