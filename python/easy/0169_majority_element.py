class Solution:

    """
    Solution via hash-map counter.

    Puts all possible elements in a dictionary as keys, with initial values of 0. Then, loop through
    all the elements, incrementing the corresponding key-value pair by 1 each time an element is
    encountered.

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        # Create dictionary
        for i in nums:
            counter[i] = 0

        # Increment element counts
        for i in nums:
            counter[i] += 1

        # Look for the largest element count, return the corresponding element
        majority_count = majority_element = 0

        for i in counter:
            if counter[i] > majority_count:
                majority_count = counter[i]
                majority_element = i

        return majority_element

