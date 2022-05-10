class Solution:
    
    """
    Solution via DP.
    
    The idea is to create an auxillary matrix with the exact same size as the original matrix.
    Each auxillary matrix element will contain the size of the largest running square that the 
    corresponding original matrix element is a part of. Once the auxillary matrix is filled, we
    simply take the maximum element of the auxillary matrix and square it to get the are of the
    largest submatrix, as required.

    Time complexity: O(mn)
    Space complexity: O(mn)
    """
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # Initialize counter matrix
        num_of_rows = len(matrix)
        num_of_cols = len(matrix[0])
        counter_matrix = [[0 for cols in range(num_of_cols)] for rows in range(num_of_rows)]
        
        # Fill first row and col of counter matrix with the elements from the original matrix
        for col in range(0, num_of_cols, 1):
            counter_matrix[0][col] = int(matrix[0][col])
        for row in range(0, num_of_rows, 1):
            counter_matrix[row][0] = int(matrix[row][0])
        
        # Calculate largest submatrix encaspulating each matrix element via memoization and dynamic programming
        for row in range(1, num_of_rows, 1):
            for col in range(1, num_of_cols, 1):
                if matrix[row][col] == "0":
                    counter_matrix[row][col] = 0
                else:
                    counter_matrix[row][col] = 1 + min(counter_matrix[row - 1][col - 1], 
                                                       counter_matrix[row - 1][col], counter_matrix[row][col - 1])
        
        # Loop through the counter matrix and find the largest number - this is the size of our desired square submatrix
        max_subarray = 0
        for row in range(0, num_of_rows, 1):
            for col in range(0, num_of_cols, 1):
                if counter_matrix[row][col] > max_subarray:
                    max_subarray = counter_matrix[row][col]
        
        # Return area of largest square submatrix
        return(max_subarray * max_subarray)