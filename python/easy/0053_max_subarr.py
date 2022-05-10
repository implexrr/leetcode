class Solution:
    
    """
    Solution via DP/divide and conquer.
    
    Solves the maximum subarray problem by tracking the sum of the current running subarray,
    resetting the current run whenever the next element has a higher value than the entire run.
    If the running sum is ever higher than best sum, that sum becomes the best sum.
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    
    def maxSubArray(self, nums: List[int]) -> int:
        best_sub = running_sub = nums[0]
        
        for i in nums[1:]:
            
            # Should we restart the current run?
            if running_sub > 0:
                running_sub += i
            else:
                running_sub = i
            
            # Is the running_subarray better than the best subarray on record?
            if running_sub > best_sub:            
                best_sub = running_sub
        return best_sub