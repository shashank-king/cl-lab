function determinant = det_recursive(matrix)
%  This function calculates the determinant of a matrix recursively.
%
 % Args:
  %    matrix: A matrix representing the input.

  %Returns:
   %   The determinant of the matrix.
  

  # Base case: 2x2 matrix
  if (rows(matrix) == 2)
    determinant = matrix(1, 1) * matrix(2, 2) - matrix(1, 2) * matrix(2, 1);
    return;
  endif;

  # Recursive case: Larger matrices
  determinant_sum = 0;
  for col = 1:columns(matrix)
    submatrix = matrix(2:rows(matrix), [1:col-1, col+1:columns(matrix)]);  # Create submatrix
    determinant_sum += matrix(1, col) * det_recursive(submatrix) * (-1)^(col-1);
  endfor;
  determinant = determinant_sum;
endfunction;

# Define your matrix (replace with your actual values)
matrix = [1 2 3; 4 5 6; 7 8 9];

# Calculate determinant using the recursive function
determinant = det_recursive(matrix);

# Print the result
printf("Determinant: %f\n", determinant);
