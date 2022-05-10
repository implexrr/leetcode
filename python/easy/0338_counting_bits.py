class Solution:
    
    """
    Solution via memoization and bit manipulation.

    Time complexity: O(n)
    Space complexity: O(n)
    """


    def countBits(self, n: int) -> List[int]:

        # Create empty counter list of 0s
        how_many_ones = [0] * (n + 1)

        # Hardcode for edge cases
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        # Initialize counter list
        how_many_ones[0] = 0
        how_many_ones[1] = 1

        # Calculate number of 1s in bit representation of integer
        for i in range(2, n + 1, 1):

            # If power of 2, number of 1s must be 1
            if ((i & (i - 1)) == 0):
                how_many_ones[i] = 1
                most_recent_power = i

            # Calculate number of 1s from previous calculations
            else:
                how_many_ones[i] = how_many_ones[most_recent_power] + how_many_ones[i - most_recent_power]
        return(how_many_ones)

