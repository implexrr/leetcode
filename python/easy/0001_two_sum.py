class Solution:
    
    """
    Solution via list enumeration and hash table.
    
    Iterates over the entire enumerated list of integers, then puts each integer into a hash table where 
    the key is the other integer needed to hit the target, and the value is the index of the original
    integer. If an integer matches a key in the dictionary, return both the index of that integer and the 
    corresponding value in the key-value pair.
    
    Time complexity: O(n)
    Space complexity: O(n)
    """
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        enumerated = enumerate(nums)
        npairs = {}
        
        for ind, n in enumerated:
            if n in npairs:
                return [npairs[n], ind]
            npairs[target - n] = ind