def det(A):
    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    determinant = 0

    # Iterate over the elements in the first row
    for j in range(len(A)):
        # Calculate the cofactor for element matrix[0][j]
        submatrix = [[A[i][k] for k in range(len(A)) if k != j] for i in range(1, len(A))]
        cofactor = (-1) ** (0 + j) * det(submatrix)  # Recursive call to calculate determinant

        # Multiply the element by its cofactor and add to the determinant
        determinant += A[0][j] * cofactor

    return determinant