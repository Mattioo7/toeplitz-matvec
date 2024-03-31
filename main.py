import numpy as np
import sys
import multiplication as mp
import matrix_parser as mpar

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

if __name__ == '__main__':
    toeplitzes, vectors = mpar.read(sys.argv[1])
    assert len(toeplitzes) == len(vectors)

    all_matching = True
    for i in range(len(toeplitzes)):
        toeplitz = toeplitzes[i]
        vector = np.array(vectors[i])
        fast_result = mp.toeplitz_vector_mult_fft(toeplitz, vector)

        print(f"Multiplication result no. {i + 1} is {fast_result}")
