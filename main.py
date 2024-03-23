import numpy as np
import sys
import multiplication as mp
import matrix_parser as mpar

if __name__ == '__main__':
    matrices, vectors = mpar.read(sys.argv[1])
    print("Matrices:", matrices)
    print("Vectors:", vectors)
    # row = np.array([1, 2, 3])  # First row of the Toeplitz matrix
    # col = np.array([1, 4, 5])  # First column of the Toeplitz matrix
    # vec = np.array([1, 2, 3])  # Vector to multiply
    # fast_result = mp.toeplitz_vector_mult_fft(col, row, vec)
    # print("Result:", fast_result)

    # classic_result = mp.normal_mult(, vec)

    # if np.allclose(fast_result, classic_result):
    #     print("The result matches the expected value.")
    # else:
    #     print("The result does not match the expected value.")
