matrix = [1 2 3; 4 5 6; 7 8 9];

if size(matrix, 1) == 2
  determinant = matrix(1, 1) * matrix(2, 2) - matrix(1, 2) * matrix(2, 1);
else
  determinant = 0;
  for col = 1:size(matrix, 2)
    submatrix = matrix(2:end, [1:col-1, col+1:end]);
    determinant += matrix(1, col) * det_recursive(submatrix) * (-1)^(col-1);
  end
end

fprintf("Determinant: %f\n", determinant);
