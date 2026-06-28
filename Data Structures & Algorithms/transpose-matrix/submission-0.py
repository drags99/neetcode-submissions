class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transposed_matric = []
        for c in range(cols):
            transposed_matric.append([None]*rows)
                

        for r in range(rows):
            for c in range(cols):
                transposed_matric[c][r] = matrix[r][c]

        return transposed_matric