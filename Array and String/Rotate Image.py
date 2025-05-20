class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # for the elements where row number is smaller than column number
                # i.e. elements above the diagonal will swap with elements below the diagonal
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row to get the final result
        for i in range(len(matrix)):
            matrix[i].reverse()
        
        return matrix