class Solution:

    """
    Solution via coutner array.
    
    Create a counter array; anytime a letter in the string is encountered, increment the corresponding
    counter array element by 1. If we loop through the string again, then the first character where
    the corresponding counter element is greater than 1 is our desired answer.

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def firstUniqChar(self, s: str) -> int:
        character_count = [0 for i in range(26)]

        for letter in s:
            character_count[(ord(letter) - 97)] += 1
        print(character_count)

        for letter_index in range(0, len(s), 1):
            if character_count[(ord(s[letter_index]) - 97)] == 1:
                return letter_index
                
        return -1