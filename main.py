import sys

import numpy as np

import matrix_parser as mpar
import multiplication as mp


def matrix_from_toeplitz(toeplitz):
    size = (int)((len(toeplitz) + 1) / 2)
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        matrix[i][0] = toeplitz[i]

    rev = list(reversed(toeplitz))
    for i in range(1, size):
        matrix[0][i] = rev[i - 1]
    for i in range(1, size):
        for j in range(1, size):
            matrix[i][j] = matrix[i-1][j-1]

    return matrix


def integers(numbers):
    return [int(num) for num in numbers]


if __name__ == '__main__':
    toeplitzes, vectors = mpar.read(sys.argv[1])
    assert len(toeplitzes) == len(vectors)

    all_matching = True
    for i in range(len(toeplitzes)):
        toeplitz = toeplitzes[i]
        vector = np.array(vectors[i])

        result_1_numpy_result = mp.toeplitz_vector_mult_fft(toeplitz, vector)
        result_2_my_fourier_result = mp.toeplitz_vector_mult_fft_custom(toeplitz, vector)
        result_3_standard_mult = mp.normal_mult(mp.matrix_from_toeplitz(toeplitz), vector)

        print(f"Using numpy   {i + 1} is {result_1_numpy_result}")
        print(f"Using my fft  {i + 1} is {result_2_my_fourier_result}")
        print(f"Standard mult {i + 1} is {result_3_standard_mult}")
