class Solution:
    """
    Solution via extra array.
    
    Create auxillary array, then make each element in the auxillary array
    the shifted version of the original array via modular arithmetic.
    
    Time complexity: O(n)
    Space complexity: O(n)
    """
    
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        rotated_arr = nums.copy()
        for i in range(n):
            rotated_arr[i] = nums[(i - k) % n]
        for i in range(n):
            nums[i] = rotated_arr[i]