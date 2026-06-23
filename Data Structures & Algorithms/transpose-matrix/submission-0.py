class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        new_matrix = []

        for i in range(0,len(matrix[0])):
            row = []
            for j in range(0,len(matrix)):
                row.append(matrix[j][i])
            new_matrix.append(row)

        return new_matrix
        