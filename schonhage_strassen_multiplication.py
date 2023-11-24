import numpy as np

def strassen_multiply_128bit(A, B):
    # Base case: If the matrices are 1x1, perform standard multiplication
    if A.shape == (1, 1):
        return A * B

    # Split matrices into quadrants
    n = A.shape[0] // 2
    A11 = A[:n, :n]
    A12 = A[:n, n:]
    A21 = A[n:, :n]
    A22 = A[n:, n:]

    B11 = B[:n, :n]
    B12 = B[:n, n:]
    B21 = B[n:, :n]
    B22 = B[n:, n:]

    # Recursive steps
    P1 = strassen_multiply_128bit(A11 + A22, B11 + B22)
    P2 = strassen_multiply_128bit(A21 + A22, B11)
    P3 = strassen_multiply_128bit(A11, B12 - B22)
    P4 = strassen_multiply_128bit(A22, B21 - B11)
    P5 = strassen_multiply_128bit(A11 + A12, B22)
    P6 = strassen_multiply_128bit(A21 - A11, B11 + B12)
    P7 = strassen_multiply_128bit(A12 - A22, B21 + B22)

    # Calculating the resulting quadrants
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6

    # Combining quadrants to get the result
    result = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return result

A = np.array([[2**64, 2**64], [2**64, 2**64]], dtype=np.uint128)
B = np.array([[2**64, 2**64], [2**64, 2**64]], dtype=np.uint128)

result = strassen_multiply_128bit(A, B)
print(result)
