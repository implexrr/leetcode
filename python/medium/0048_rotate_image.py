class Solution:
    """
    Solution via array manipulation.
    
    Swap elements around the matrix, one layer/ring at a time.
    
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        num_of_rings = int(n/2)
        
        for ring in range(num_of_rings):
            swaps = n - 1 - (2 * ring)
            
            for swap in range(swaps):
                temp = matrix[ring][ring + swap]
                matrix[ring][ring + swap] = matrix[n - 1 - ring - swap][ring]
                matrix[n - 1 - ring - swap][ring] = matrix[n - 1 - ring][(n - 1) - ring - swap]
                matrix[n - 1 - ring][(n - 1) - ring - swap] = matrix[ring + swap][n - 1 - ring]
                matrix[ring + swap][n - 1 - ring] = temp