class Solution:
    """
    Solution via hash table counter.
    Add characters for first word into a dictionary as keys, setting the value to 0.
    Looping through the first word again, increment the value for each corresponding
    character in the dictionary by 1. Loop through the 2nd word and decrement the
    value for each corresponding character in the dictionary by 1 (if it exists at all).
    If we dont end up with a dictionary of all 0s at the end, then the words aren't
    anagrams of each other.

    """
    def isAnagram(self, s: str, t: str) -> bool:
        #add characters for word 1 to dictionary, i.e. a == true, n == true, etc
        #loop through character 2; if the key in the dictionary exists, go to that key and remove
        #the the dictionary entry
        #return true iff the dictionary is empty
        if len(s) != len(t):
            return False

        is_anagram = {}

        for key in s:
            is_anagram[key] = 0

        for key in s:
            is_anagram[key] += 1

        for key in t:
            if key in is_anagram:
                is_anagram[key] -= 1
            else:
                return False