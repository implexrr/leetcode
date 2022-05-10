class Solution:
    
    """
    Solution via list memoization.
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = []
        sums.append(nums[0])
        for i in range(1, len(nums)):
            sums.append(sums[i - 1] + nums[i])
        return sums