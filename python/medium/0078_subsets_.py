class Solution:
    """
    Solution via backtracking?

    Create the powerset by iterating through every element in the original set, and appending
    that element to the end of every subset currently in the power set.

    Time complexity: O((n!)(n^2))
    Space complexity: O(n!)?
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        for i in range(len(nums)):
            for j in range(len(results)):
                results.append(results[j] + [nums[i]])
        return results