class Solution:

    """
    Solution via hash table.

    Loop through the array once. For each element, we either add it to the
    hash table or return true if its already in the hash table. If we make
    it to the end of the loop without encountering a duplicate, return false.

    Time complexity: O(n)
    Space complexity: O(n)
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate_check = {}

        for i in nums:
            if (i in duplicate_check):
                return True
            else:
                duplicate_check[i] = True

        return False