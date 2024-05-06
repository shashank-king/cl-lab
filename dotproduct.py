# Define two vectors
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

# Check if the vectors have the same length
if len(vector1) != len(vector2):
    print("Error: Vectors must have the same length.")
else:
    # Initialize the dot product
    dot_product = 0
    # Calculate the dot product
    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]

    print("Dot product of the two vectors:", dot_product)

