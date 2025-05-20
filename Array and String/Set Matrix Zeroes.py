class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = {}
        rows = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # if the element is 0, update the row and column number the hash set
                if matrix[i][j] == 0:
                    rows.update({i : 0})
                    cols.update({j : 0})
                    # nums[i][0] = -1
                    # nums[0][j] = -1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                # if the row or column number is present in the dict
                # update the element to value 0
                if i in rows or j in cols:
                    matrix[i][j] = 0

        return matrix
