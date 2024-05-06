def determinant(matrix):
  if len(matrix) == 2:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
  determinant_sum = 0
  for col in range(len(matrix)):
    submatrix = [row[:col] + row[col+1:] for row in matrix[1:]]  # Create submatrix
    determinant_sum += matrix[0][col] * determinant(submatrix) * (-1) ** col
  return determinant_sum
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
determinant = determinant(matrix)
print("Determinant:", determinant)
