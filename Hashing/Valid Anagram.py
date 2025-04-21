class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_set = {}
        count = 0

        # Store all the character's number of appearance
        for char in s:
            if char not in hash_set:
                hash_set[char] = hash_set.get(char, 0) + 1
            else:
                hash_set[char] += 1

        for char in t:
            # if char from t is present in hash_set
            # decrement the count in hash_set
            if char in hash_set:
                hash_set[char] -= 1
                count += 1
                # If the character's count becomes 0, remmove it from dict
                if hash_set[char] == 0:
                    del hash_set[char]
            else:
                return False
        
        # if hash_set becomes empty 
        if not hash_set:
            return True
        else:
            return False