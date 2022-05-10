class Solution:
    
    """
    Solution via (just looking at the question??)
    
    Time complexity: O(n)
    Space complexity: O(1)
    """
    
    def minPartitions(self, n: str) -> int:
        min_needed = 0
        for i in n:
            if (int(i) > min_needed):
                min_needed = int(i)
            if (i == '9'):
                return 9
        return min_needed