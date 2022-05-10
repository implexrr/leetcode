class Solution:

    """
    Solution via backtracking.

    Create all possible permutations by treating the generation of any given permutation
    like going down a path. Once a permutation slot has been filled with an element, the
    element is removed from the list of possible elements and the next slot is filled with
    one of the remaining elements. Each chosen element is a pivot. Once all elements have
    been exhausted, we have a permutation, which is then added to the list of all possible
    permutations. This process is then repeated every possible pivot.

    Time complexity: O((n!)(n^2))?
    Space complexity: O(n!(n))?
    """

    # Initialize results list
    def __init__(self):
        self.results = []

    # Generate all possible permutations of nums list via the path_creator function and an initially empty path.
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.path_creator(nums, [])
        return self.results

    # Create a path; each time a number is added to the path, the number is removed from the set of possible remaining numbers
    def path_creator(self, unvisited, path):
        if (not unvisited):
            self.results.append(path)
        for n in range(len(unvisited)):
            self.path_creator(unvisited[:n] + unvisited[n + 1:], path + [unvisited[n]])