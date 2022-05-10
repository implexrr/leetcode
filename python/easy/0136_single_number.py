class Solution:
    
    """
    Solution via bit manipulation.

    1. a XOR 0 == a
    2. a XOR a == 0
    3. Bitwise operators like AND, OR and XOR are both commutative and associative.

    Based on the 3 statements above, any string of pairs + one unique character, such as abbacdcegffed,
    can be rewritten as (aabbccddeeff)g, which == (0)g which == g, as required.

    Time complexity: O(n)
    Space complexity: O(1)
    """

    def singleNumber(self, nums: List[int]) -> int:

        unique = 0
        for i in nums:
            unique ^= i
        return unique

    """
    Solution via hash table.

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def singleNumber2(self, nums: List[int]) -> int:
        # Creating empty hash table
        counter_dict = {}

        # If no entry exists for the list number, add it. If it's already there, remove it.
        for i in nums:
            if counter_dict.get(i) == True:
                counter_dict.pop(i)
            else:
                counter_dict[i] = True

        # The unique number should be the key of the only dictionary entry left.
        return(next(iter(counter_dict)))
