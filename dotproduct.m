% Define two vectors
vector1 = [1, 2, 3];
vector2 = [4, 5, 6];

% Check if the vectors have the same length
if length(vector1) != length(vector2)
    disp("Error: Vectors must have the same length.");
else
    % Initialize the dot product
    dot_product = 0;
    % Calculate the dot product
    for i = 1:length(vector1)
        dot_product += vector1(i) * vector2(i);
    end

    disp(["Dot product of the two vectors:", num2str(dot_product)]);
end
